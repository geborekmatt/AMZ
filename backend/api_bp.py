from flask import Blueprint
import keepa
import requests
import pandas as pd
from input_csv_formating import convert_csv_file, format_product_input_price_df
from os import listdir, replace

api_bp = Blueprint('api_routes', __name__)



@api_bp.route('/api/test_api_bp', methods=['POST'])
def index():

    return "tested api bp"