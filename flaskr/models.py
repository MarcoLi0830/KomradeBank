import os
import json
import bcrypt
import uuid
import hashlib

class KomradeConfig:
    def __init__(self, name):
        self.config_file = os.path.join(os.path.dirname(__file__), "../" + name + ".json")

        if not os.path.exists(self.config_file):
            open(self.config_file, "w").write("{}")

    def read(self):
        return json.loads(open(self.config_file, "r").read())

    def write(self, data):
        with open(self.config_file, 'w') as fh:
            fh.write(json.dumps(data))

def registerUser(username, password):
    komrade = KomradeConfig("user")
    if checkIfExisted(username, komrade):
        return 0
    userPass = komrade.read()
    userPass[username]=password
    #print('list:',userPass)
    komrade.write(userPass)
    return True

def checkIfExisted(username,komrade):
    userPass = komrade.read()
    #print('list:',userPass)
    if username in userPass.keys():
        return True
    
    return False


def validateUser(username, password):
    komrade = KomradeConfig("user")
    userPass = komrade.read()
    if username in userPass.keys():
        if password == userPass[username]:
            return True
    return False

def md5Encrypt(str):
    md5 = hashlib.md5()
    md5.update(str)
    #print("md5: ",md5.hexdigest())
    return md5.hexdigest()
