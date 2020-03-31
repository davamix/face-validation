import torch
from database import Database
from models.user import User

class UserService():
    # def __init__(self):
    #     pass

    def get_user_embeddings(self, username):
        params = (username,)
        query = "SELECT value FROM embeddings WHERE username = ?"

        results = Database().execute(query, params)
        results = torch.FloatTensor(results)
        
        return results

    # def save_user(self, user):
    #     params = (user.username, user.embedding,)
    #     query = "INSERT INTO user (username, embedding) VALUES (?,?)"

    #     result = Database().execute(query, params)
    #     print(result) # None
        