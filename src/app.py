from flask import Flask
from flask_restful import Api
# controllers
from src.controllers.home_controller import home_page
#from flask_bootstrap import Bootstrap5

from src.controllers.apis.blueprint_api_config import api_register
app = Flask(__name__, static_folder=None)


'''the bootstrap init'''
#bootstrap = Bootstrap5(app)

app.register_blueprint(api_register)


app.register_blueprint(home_page,url_prefix='/')
