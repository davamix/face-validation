from database import Database
from models.user import User

class UserService():
    def __init__(self):
        pass

    def get_user(self, username):
        params = (username,)
        query = "SELECT username, embedding FROM user WHERE username = ?"

        result = Database().execute(query, params)
        print(result)

    def save_user(self, user):
        params = (user.username, user.embedding,)
        query = "INSERT INTO user (username, embedding) VALUES (?,?)"

        result = Database().execute(query, params)
        print(result) # None
        