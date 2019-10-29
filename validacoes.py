from mongoDB import *

class Validacao:

    def username_existe(self, username):
        db = MongoConnect()
        result = db.find_one({"username": username})

        if result:
            return True
        return False

    def username_password_valido(self, data):
        db = MongoConnect()
        result = db.read({"username": data["username"]})

        if result["username"] == data["username"] and result["password"] == data["password"]:
            return True
        return False






