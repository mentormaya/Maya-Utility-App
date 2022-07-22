import sqlite3

class DB():
    def __init__(self, name = "database.db"):
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        # self.initTables()
        
    def __del__(self):
        self.connection.commit()
        self.connection.close()
        
    
    def initTables(self):
        query = """
            CREATE TABLE IF NOT EXISTS Configs(
                
            )
        """
        print("Initializing Tables Structure")
        print(query)