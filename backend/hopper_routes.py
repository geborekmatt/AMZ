from flask import Blueprint, request
import pandas as pd
from input_csv_formating import format_product_input_price_df
from os import listdir, replace,path
from db import pool
hopper_bp = Blueprint('hopper_routes', __name__)

@hopper_bp.route('/api/run_hopper', methods=['POST'])
def run_hopper():
    try :
        con = pool.getconn()
        cur = con.cursor()
        payload = request.get_json()
        hopper_config = payload['hopperConfig']
        ### Insert files from input_product_csvs folder into db and move to added_input_product_csvs
        path_to_input_folder = "input_product_csvs" #Need to add these to config backend\input_product_csvs
        path_to_input_folder = "input_product_csvs"
        path_to_added_input_folder = "added_input_product_csvs" 
        
        csv_names = [f for f in listdir(path_to_input_folder) if f.endswith(".csv")]

        formatted_input_csv_dfs = []
        for csv_name in csv_names:
            ##opened_csv_df = pd.read_csv(f"{path_to_input_folder}{csv_name}")
            opened_csv_df = pd.read_csv(path.join(path_to_input_folder,csv_name))
            df_price_formatted = format_product_input_price_df(opened_csv_df)
            df_columns_formatted = df_price_formatted[['PRODUCT_URL','PRODUCT_TITLE','PRODUCT_PRICE','PRODUCT_BRAND']]
            formatted_input_csv_dfs.append(df_columns_formatted)
            df_combined_csvs = pd.concat(formatted_input_csv_dfs)
        df_combined_csvs.reset_index(drop=True,inplace=True)
        df_combined_csvs.drop_duplicates(inplace=True)

        #Filter hopper products by ignored brands
        if any(val is True for val in hopper_config.values()) :
            brands_to_ignore_query = "select * from brand where disabled = false or possible_ip = false or approved = 0;"

            cur.execute(brands_to_ignore_query)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            df = pd.DataFrame(data=rows,columns =colnames )

            brands_to_ignore = []
            if hopper_config['includeBrandAliases'] == True:
                for aliases in df['aliases']:
                    brands_to_ignore = [*brands_to_ignore, *aliases]
                    brands_to_ignore = list(filter(lambda x: x!="", brands_to_ignore))
                brands_to_ignore = [*brands_to_ignore, *df['name'].to_list()]
            else :
                brands_to_ignore = df['name'].to_list()
            
            df_combined_csvs = df_combined_csvs.loc[~df_combined_csvs['PRODUCT_BRAND'].isin(brands_to_ignore),:]

            products_to_add = df_combined_csvs.to_dict(orient='records')
            product_insert_base_query = "INSERT INTO product(title,url,price,searched) VALUES "
            product_inserts= []
            for product in products_to_add:
                product_insert = f"('{product['PRODUCT_TITLE']}', '{product['PRODUCT_URL']}',{product['PRODUCT_PRICE']}, false)"
                product_inserts.append(product_insert)
            product_insert_query = product_insert_base_query + ", ".join(product_inserts) + ';'
            
            cur.execute(product_insert_query)
            cur.close()
            con.commit()
            pool.putconn(con) 

        for csv_name in csv_names:
            replace(f"{path.join(path_to_input_folder,csv_name)}", f"{path.join(path_to_added_input_folder,csv_name)}")
        return "Hopper successful",200
    except Exception as e :
        print(e)
        cur.close()
        pool.putconn(con) 
        return "error", 400

@hopper_bp.route('/api/input_files', methods=['GET'])
def get_input_files():
    try :
        path_to_input_folder = "input_product_csvs" #Need to add these to config backend\input_product_csvs
        csv_names = [f for f in listdir(path_to_input_folder) if f.endswith(".csv")]
        files = []
        for csv_name in csv_names:
            opened_csv_df = pd.read_csv(path.join(path_to_input_folder,csv_name))
            file = {}
            file['name'] = f"{csv_name}"
            file['product_count'] = len(opened_csv_df)
            files.append(file)
        return files, 200
    except Exception as e:
        return {'error': str(e)},400

@hopper_bp.route('/api/hopper_status', methods=['GET'])
def get_hopper_status():
    try :
        path_to_input_folder = "input_product_csvs" #Need to add these to config backend\input_product_csvs
        input_csv_names = [f for f in listdir(path_to_input_folder) if f.endswith(".csv")]
        hopper_status = {'input_file_count': 0, 'added_file_count':0, 'input_file_product_count':0}
        for csv_name in input_csv_names:
            opened_csv_df = pd.read_csv(path.join(path_to_input_folder,csv_name))
            hopper_status['input_file_product_count'] += len(opened_csv_df)
            hopper_status['input_file_count'] += 1

        input_csv_names = [f for f in listdir(path_to_input_folder) if f.endswith(".csv")]
        path_to_added_input_folder = "added_input_product_csvs" 
        added_csv_names = [f for f in listdir(path_to_added_input_folder) if f.endswith(".csv")]
        hopper_status['added_file_count'] += len(added_csv_names)
        return hopper_status, 200
    except Exception as e:
        return {'error': str(e)},400