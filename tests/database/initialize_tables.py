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

    def test_user_table_is_created(self):
        expected = [("user", )]
        
        conn = sqlite3.connect("file:test1?mode=memory&cache=shared")
        db = Database("file:test1?mode=memory&cache=shared")
        db.initialize_tables()

        results = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")

        self.assertCountEqual(expected, results)


