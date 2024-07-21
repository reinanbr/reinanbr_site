from flask import Blueprint


# Defining a blueprint
home_page = Blueprint(
    'home', __name__,
    template_folder='templates',
    static_folder='static')

