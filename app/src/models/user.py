from database import Database

class User():
    def __init__(self, username = None, embedding = None):
        self.username = username
        self.embedding = embedding

        # self.__create_table()

    # def __create_table(self):
    #     query = "CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL UNIQUE, embedding REAL)"
    #     Database().execute(query)