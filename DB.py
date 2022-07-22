import sqlite3

class DB():
    def __init__(self, name = "database.db"):
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()