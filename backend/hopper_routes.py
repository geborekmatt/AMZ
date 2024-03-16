from flask import Blueprint, request
import pandas as pd
from input_csv_formating import format_product_input_price_df
from os import listdir, replace,path

hopper_bp = Blueprint('hopper_routes', __name__)

@hopper_bp.route('/api/run_hopper', methods=['POST'])
def run_hopper():
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
        df_columns_formatted = df_price_formatted[['PRODUCT_URL','PRODUCT_TITLE','PRODUCT_PRICE']]
        formatted_input_csv_dfs.append(df_columns_formatted)
        df_combined_csvs = pd.concat(formatted_input_csv_dfs)
    df_combined_csvs.reset_index(drop=True,inplace=True)
    df_combined_csvs.drop_duplicates(inplace=True)

    #Insert input file products into Product table

    for csv_name in csv_names:
        replace(f"{path.join(path_to_input_folder,csv_name)}", f"{path.join(path_to_added_input_folder,csv_name)}")
    return "Hopper successful"

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