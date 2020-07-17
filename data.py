
# data.py
from flask import Blueprint
public_data = Blueprint("public", __name__,
    static_url_path='/public', static_folder='./public'
    )
