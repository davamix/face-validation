from pathlib import Path
import unittest
import sqlite3

from src.database import Database

class TestInitializeTables(unittest.TestCase):
    def setUp(self):
        connection_string = "file:testdb?mode=memory&cache=shared"

        self.conn = sqlite3.connect(connection_string)
        self.db = Database(connection_string)

        self.conn.execute("CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL UNIQUE, embedding REAL)")

    def tearDown(self):
        self.conn.close()

        # Remove temp database
        Path("file").unlink()

    def test_insert_user(self):
        expected = ("Me", 0.123456789, )

        self.db.execute("INSERT INTO user(username, embedding) VALUES (?, ?)", params=["Me", 0.123456789])
        results = self.conn.execute("SELECT * FROM user")

        self.assertCountEqual(expected, results.fetchone())

    def test_select_user(self):
        expected = [("Me", 0.123456789, )]

        # self.conn.execute("INSERT INTO user(username, embedding) VALUES (?, ?)", ("Me", 0.123456789,))
        self.db.execute("INSERT INTO user(username, embedding) VALUES (?, ?)", params=["Me", 0.123456789])
        results = self.db.execute("SELECT * FROM user")

        self.assertCountEqual(expected, results)