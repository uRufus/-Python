import json
import sqlite3

from framework.data_mapper import UserMapper, AuthMapper

check_user = UserMapper(sqlite3.connect('framework/project_db'))
auth = AuthMapper(sqlite3.connect('framework/project_db'))

def login(addr, log_in=None, password=None):
    check_auth = auth.find_by_addr(addr)
    if check_auth:
        return check_auth[1]
    try:
        ch_usr = check_user.find_by_login(log_in)
        if ch_usr is not None and ch_usr[1] == password:
            auth.insert({addr:ch_usr[0]})
            return ch_usr[0]
        else:
            return None
    except KeyError:
        return None


def logout(addr):
    auth.delete(addr)
    return None
