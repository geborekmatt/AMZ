from flask import Blueprint, request
import pandas as pd
from db import pool
from psycopg2.extras import RealDictCursor
products_bp = Blueprint('product_routes', __name__)

@products_bp.route('/api/products', methods=['GET'])
def get_products():
    try: 
        con = pool.getconn()
        cur = con.cursor()
        cur.execute("select * from product;")
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data=rows,columns =colnames )
        cur.close()
        pool.putconn(con) 
        products = df.to_dict(orient='records')
        return products, 200
    except Exception as e:
        pool.putconn(con) 
        return {"error": str(e)}, 400