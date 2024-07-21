import json

from config import PATH_JSON_DB

def read_json():
    db_json = json.load(open(PATH_JSON_DB,'r'))
    return db_json



def add_access(user_info):
    new_db = read_json()
    new_db['access'].append(user_info)
    json.dump(new_db,open(PATH_JSON_DB,'w'),indent=4)

