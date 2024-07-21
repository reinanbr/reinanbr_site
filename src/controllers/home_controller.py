from flask import render_template,request
from src.views.home import home_page


@home_page.route('/',methods=['get'])
def index():
    userAgent = request.headers.get('User_Agent').lower()
    is_mobile=''
    return render_template('index.html'),200

