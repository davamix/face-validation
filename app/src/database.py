import sqlite3
from pathlib import Path

from services.configuration import ConfigurationService

class Database():
    def __init__(self):
        self.__db_path = ConfigurationService().get_connection_string()

    # def initialize_tables(self):
    #     create_user_table_query = "CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL UNIQUE)"
    #     create_embeddings_table_query = "CREATE TABLE IF NOT EXISTS embeddings(username TEXT, value REAL)"
    #     insert_user_query = "INSERT INTO user(username) VALUES (?)"
    #     # self.execute(query)
    #     self.execute_many([create_user_table_query, create_embeddings_table_query])
    #     self.execute(insert_user_query, params=("Me",))

    def execute(self, query, params=None):
        
        conn = sqlite3.connect(self.__db_path)

        try:
            with conn:
                cursor = conn.cursor()

                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                return cursor.fetchall()

        except sqlite3.IntegrityError as ex:
            print(f"ERROR: {ex}")

    def execute_many(self, queries):
        conn = sqlite3.connect(self.__db_path)

        try:
            with conn:
                cursor = conn.cursor()

                for q in queries:
                    cursor.execute(q)

        except sqlite3.IntegrityError as ex:
            print(f"ERROR: {ex}")