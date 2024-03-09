from flask import Blueprint
import keepa
import requests
import pandas as pd
from input_csv_formating import convert_csv_file, format_product_input_price_df
from os import listdir, replace
from db import conn
from psycopg2.extras import RealDictCursor
api_bp = Blueprint('api_routes', __name__)



@api_bp.route('/api/test_api_bp', methods=['POST'])
def index():
    cur = conn.cursor()
    # cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("select * from brand")
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data=rows,columns =colnames )
    print(df)
    conn.close()
    print(colnames)
    return "tested api bp"