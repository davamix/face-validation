import sqlite3
from pathlib import Path

class Database():
    def __init__(self, db_path):
        # p = Path(Path.cwd(), "data")
        # p.mkdir(parents=True, exist_ok=True)
        
        # self.__db_path = p.joinpath("users.db")
        self.__db_path = db_path

    def initialize_tables(self):
        query = "CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL UNIQUE, embedding REAL)"
        
        self.execute(query)

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