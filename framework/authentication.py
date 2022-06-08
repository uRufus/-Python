import json


# def authentication(addr):
#     with open('framework/file_db/authentication.json', mode='r') as f:
#         auth = json.load(f)
#     if addr in auth:
#         return auth[addr]
#     return None

def login(addr, log_in=None, password=None):
    with open('framework/file_db/authentication.json', mode='r') as f:
        auth = json.load(f)
    if addr in auth:
        return auth[addr]
    try:
        with open('framework/file_db/users.json', mode='r') as f:
            users = json.load(f)
            if users[log_in] != password:
                return None
            with open('framework/file_db/authentication.json', mode='w') as f:
                auth[addr] = log_in
                json.dump(auth, f)
                return auth[addr]
    except KeyError:
        return None


def logout(addr):
    with open('framework/file_db/authentication.json', mode='r') as f:
        auth = json.load(f)
    with open('framework/file_db/authentication.json', mode='w') as f:
        print(auth)
        del auth[addr]
        print(auth)
        if not auth:
            auth = {}
        json.dump(auth, f)
        return None
