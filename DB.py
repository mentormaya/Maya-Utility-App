import sqlite3

class DB():
    def __init__(self, name = "database.db", _status_bar = None):
        self.name = name
        self.status_bar = _status_bar
        try:
            self.connection = sqlite3.connect(self.name)
        except sqlite3.Error as e:
            self.update("Error Occured!")
        else:
            self.update("Database Connected Successfully!")
            self.cursor = self.connection.cursor()
            self.initTables()
    
    def update(self, msg):
        msg = f'DB Update: {msg}'
        print(msg)
        if self.status_bar:
            self.status_bar.setText(msg)
        
    def __del__(self):
        self.connection.commit()
        self.update("Closing Database!")
        self.connection.close()
        
    
    def initTables(self):
        # self.initSettings()
        # self.connection.commit()
        pass
    
    def initSettings(self):
        drop_query = f"DROP TABLE IF EXISTS Configs;"
        self.cursor.execute(drop_query)
        init_table_query = """
            CREATE TABLE IF NOT EXISTS Configs(
                setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
                setting_name TEXT NOT NULL UNIQUE,
                setting_desc TEXT,
                setting_value TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """
        self.cursor.execute(init_table_query)
        self.update("Tables Structure Initialized...")
        
        settings_init_values = """
            INSERT INTO Configs(setting_name, setting_desc, setting_value)
            VALUES
            ('APP_NAME', 'Name for your APP to display.', 'v1.0.0'),
            ('COPY_TEXT', 'Copyright Text to dispaly.', 'Copyright@'),
            ('COPYRIGHT_YEAR', 'Copyright Year to dispaly.', '2022'),
            ('COPYRIGHT', 'Name of Copyright owner to display.', 'Ajay Singh'),
            ('CREDIT_TEXT', 'Credit Text to display.', 'Ajay Singh'),
            ('AUTHOR', 'Name of the Author to display.', 'Ajay Singh'),
            ('ICON', 'Path to your icon for the APP.', 'assets/icon.ico'),
            ('TESSERACT_EXE_PATH', 'Path to your Tesseract Installation on your Computer.', 'C:\\Users\\A00172\\AppData\\Local\\Tesseract-OCR\\tesseract.exe')
        """
        self.cursor.execute(settings_init_values)
        self.update("Default Settings Initialized...")
    
    def getData(self, _table, _ID_COL, _data = 0):
        if int(_data) > 0:
            get_query = f"""
                SELECT * FROM {_table} WHERE `{_table}`.`{_ID_COL} = {_data};
            """
        else:
            get_query = f"SELECT * FROM {_table};"
        self.cursor.execute(get_query)
        data = self.cursor.fetchall()
        self.update("Data Found...")
        return data