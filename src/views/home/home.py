from flask import Blueprint


# Defining a blueprint
home_page = Blueprint(
    'home', __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static',
     static_url_path='static')

