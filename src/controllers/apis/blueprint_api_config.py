from flask import Blueprint
from flask import request, jsonify
from datetime import datetime
import pytz
from tools.web.get_info_access import get_access_info
from tools.db.json import add_access_sites_db_json
# Defining a blueprint
api_register = Blueprint('api', __name__,url_prefix='/api')


#monitoring
prefix_monitoring = '/monitoring'

##sites
@api_register.route(prefix_monitoring+'/sites',methods=['post'])
def get_monitoring_sites_post():
    local_tz = pytz.timezone('America/Sao_Paulo')  # Ajuste o fuso horário conforme necessário
    now = datetime.now(local_tz)
    hour = now.strftime('%H:%M:%S')
    date = now.strftime('%d/%m/%Y')
    #print(request.get_json())
    response = request.get_json().get('infoAccess',None)
    if response:
        response['date'] = date
        response['hour'] = hour
        add_access_sites_db_json(response)
        return jsonify({"status":"ok"})
    else:
        return jsonify({"status":"false"})



#test
@api_register.route('/info_user',methods=['get'])
def get():
    user_info = get_access_info(request)
    return {"data":user_info}

