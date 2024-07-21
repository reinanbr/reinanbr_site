from flask import Flask
from flask_restful import Api
# controllers
from src.controllers.home_controller import home_page
#from flask_bootstrap import Bootstrap5

from src.controllers.apis.return_info_api_controller import api_info_user

app = Flask(__name__)
api = Api(app)

'''the bootstrap init'''
#bootstrap = Bootstrap5(app)

app.register_blueprint(api_info_user)
app.register_blueprint(home_page,url_prefix='/')
