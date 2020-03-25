import unittest
import sqlite3

from src.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")

        cursor = self.conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL UNIQUE, embedding REAL)"

        cursor.execute(query)
        self.conn.commit()

    def execute_insert(self):
        connection = sqlite3.connect(":memory:")
        cursor = self.conn.cursor()

        query = "INSERT INTO user"

