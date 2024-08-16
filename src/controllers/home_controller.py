from flask import render_template,request
from src.views.home import home_page
from tools.web.get_info_access import get_access_info
from tools.db.json import add_access

@home_page.route('/',methods=['get'])
def index():
    user_info = get_access_info(request)
    #add_access(user_info)
    is_mobile=''
    return render_template('index.html'),200

