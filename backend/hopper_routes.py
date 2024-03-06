from flask import Blueprint
import pandas as pd
from input_csv_formating import format_product_input_price_df
from os import listdir, replace

hopper_bp = Blueprint('hopper_routes', __name__)

@hopper_bp.route('/api/run_hopper', methods=['POST'])
def run_hopper():
    ### Insert files from input_product_csvs folder into db and move to added_input_product_csvs
    path_to_input_folder = "input_product_csvs\\" #Need to add these to config backend\input_product_csvs
    path_to_added_input_folder = "added_input_product_csvs\\" 
    # breakpoint()
    csv_names = [f for f in listdir(path_to_input_folder) if f.endswith(".csv")]
    print(len(csv_names))
    # breakpoint()
    formatted_input_csv_dfs = []
    for csv_name in csv_names:
        opened_csv_df = pd.read_csv(f"{path_to_input_folder}{csv_name}")
        df_price_formatted = format_product_input_price_df(opened_csv_df)
        df_columns_formatted = df_price_formatted[['PRODUCT_URL','PRODUCT_TITLE','PRODUCT_PRICE']]
        formatted_input_csv_dfs.append(df_columns_formatted)
    df_combined_csvs = pd.concat(formatted_input_csv_dfs)
    df_combined_csvs.reset_index(drop=True,inplace=True)
    df_combined_csvs.drop_duplicates(inplace=True)

    print("Formatted CSVS Results:::::")
    print(df_combined_csvs)
    #Move read csvs to  history folder
    print("Moving Read CSVS")
    #Add products to Products table

    for csv_name in csv_names:
        replace(f"{path_to_input_folder}{csv_name}", f"{path_to_added_input_folder}{csv_name}")
    return "Hopper successful"