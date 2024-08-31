import json

from config import PATH_ACCESS_SITES_JSON_DB

def read_access_sites_db_json():
    db_json = json.load(open(PATH_ACCESS_SITES_JSON_DB,'r'))
    return db_json



def add_access_sites_db_json(user_info):
    new_db = read_access_sites_db_json()
    new_db['access'].append(user_info)
    json.dump(new_db,open(PATH_ACCESS_SITES_JSON_DB,'w'),indent=4)

