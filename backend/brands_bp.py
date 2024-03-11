from flask import Blueprint, request
import pandas as pd
from db import conn
from psycopg2.extras import RealDictCursor
brands_bp = Blueprint('brands_routes', __name__)

@brands_bp.route('/api/brands', methods=['GET'])
def get_brands():
    try: 
        cur = conn.cursor()
        cur.execute("select * from brand")
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data=rows,columns =colnames )
        cur.close()
        brands = df.to_dict(orient='records')
        return brands, 200
    except Exception as e:
        return {"error": str(e)}, 400
    
@brands_bp.route('/api/brands/add', methods=['POST'])
def add_brand():
    try: 
        cur = conn.cursor()
        payload = request.get_json()
        brand = payload.get('newData')
        if brand['aliases'] is not None: 
            brand['aliases'] = brand['aliases'].split(",")
        else :
            brand['aliases'] = [""]
        query = f"INSERT INTO brand (NAME,aliases,gated,possible_ip,disabled) VALUES ('{brand['name']}', ARRAY{brand['aliases']}, {brand['gated']}, {brand['possible_ip']}, {brand['disabled']});"
        cur.execute(query)
        cur.close()
        conn.commit()
        return {"data":"Brand Added"}, 200
    except Exception as e:
        print(e)
        cur.close()
        return {"error": str(e)}, 400
@brands_bp.route('/api/brands/edit', methods=['POST'])
def edit_brand():
    try :
        cur = conn.cursor()
        payload = request.get_json()
        brand = payload.get('newData')
        if type(brand['aliases']) == type(""):
            brand['aliases'] = brand['aliases'].split(",")
        query = f"update brand set name = '{brand['name']}', aliases = ARRAY{brand['aliases']}, gated={brand['gated']}, possible_ip={brand['possible_ip']}, disabled={brand['disabled']} where id = {brand['id']};"
        cur.execute(query)
        conn.commit()
        return {"data": "Brand Edited"}, 200
    except Exception as e:
        cur.close()
        return {"error": str(e)}, 400

@brands_bp.route('/api/brands/delete', methods=['POST'])
def delete_brand():
    try :
        cur = conn.cursor()
        payload = request.get_json()
        id = payload.get('id')
        query = f"delete from brand where id = {id};"
        cur.execute(query)
        conn.commit()
        return {"data": "Brand Deleted"}, 200
    except Exception as e:
        cur.close()
        return {"error": str(e)}, 400