import pandas as pd
import openpyxl
import numpy
def find_min_price(row):
    # breakpoint()
    prices = []
    cols = ['Price','Price1','Price2','Price3','Price4','Price5']
    for col in cols:
        if col in row:
            col_price = str(row[col])
            if col_price != 'nan':
                formatted_col = col_price.replace('$','')
                col_price = float(formatted_col)
                prices.append(col_price)
    return min(prices)

def convert_csv_file(csv_file):
    df = pd.read_excel(csv_file)
    df['current_price'] = df.apply(lambda row : find_min_price(row),axis=1 )
    return df.to_dict(orient='records')

def format_product_input_price_df(df):
    df['PRODUCT_PRICE'] = df.apply(lambda row : find_min_price(row),axis=1 )
    return df



