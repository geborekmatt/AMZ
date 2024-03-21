from flask import Blueprint, request
import pandas as pd
from db import pool
from psycopg2.extras import RealDictCursor
brands_bp = Blueprint('brands_routes', __name__)

@brands_bp.route('/api/brands', methods=['GET'])
def get_brands():
    try: 
        con = pool.getconn()
        cur = con.cursor()
        cur.execute("select * from brand")
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data=rows,columns =colnames )
        df.approved = df.approved.fillna('')
        cur.close()
        pool.putconn(con) 
        brands = df.to_dict(orient='records')
        return brands, 200
    except Exception as e:
        pool.putconn(con) 
        return {"error": str(e)}, 400
    
@brands_bp.route('/api/brands/add', methods=['POST'])
def add_brand():
    try: 
        con = pool.getconn()
        cur = con.cursor()
        payload = request.get_json()
        brand = payload.get('newData')
        if brand['aliases'] is not None: 
            brand['aliases'] = brand['aliases'].split(",")
        else :
            brand['aliases'] = [""]
        if brand['approved'] == None :
            brand['approved'] = 'NULL'
        query = f"INSERT INTO brand (NAME,aliases,approved,possible_ip,disabled) VALUES ('{brand['name']}', ARRAY{brand['aliases']}, {brand['approved']}, {brand['possible_ip']}, {brand['disabled']});"
        cur.execute(query)
        cur.close()
        con.commit()
        pool.putconn(con) 
        return {"data":"Brand Added"}, 200
    except Exception as e:
        cur.rollback()
        pool.putconn(con) 
        return {"error": str(e)}, 400
@brands_bp.route('/api/brands/edit', methods=['POST'])
def edit_brand():
    try :
        con = pool.getconn()
        cur = con.cursor()
        payload = request.get_json()
        brand = payload.get('newData')
        if type(brand['aliases']) == type(""):
            brand['aliases'] = brand['aliases'].split(",")
        if brand['approved'] in ('', None) :
            brand['approved'] = 'NULL'
        query = f"update brand set name = '{brand['name']}', aliases = ARRAY{brand['aliases']}, approved = {brand['approved']}, possible_ip={brand['possible_ip']}, disabled={brand['disabled']} where id = {brand['id']};"
        cur.execute(query)
        con.commit()
        pool.putconn(con) 
        return {"data": "Brand Edited"}, 200
    except Exception as e:
        cur.rollback()
        pool.putconn(con) 
        return {"error": str(e)}, 400

@brands_bp.route('/api/brands/delete', methods=['POST'])
def delete_brand():
    try :
        con = pool.getconn()
        cur = con.cursor()
        payload = request.get_json()
        id = payload.get('id')
        query = f"delete from brand where id = {id};"
        cur.execute(query)
        con.commit()
        pool.putconn(con) 
        return {"data": "Brand Deleted"}, 200
    except Exception as e:
        cur.rollback()
        pool.putconn(con) 
        return {"error": str(e)}, 400