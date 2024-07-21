from flask import request
from src.controllers.apis.blueprint_api_config import api_config
from tools.web.get_info_access import get_access_info

api_info_user = api_config

@api_info_user.route('/info_user',methods=['get'])
def get():
    user_info = get_access_info(request)
    return {"data":user_info}


