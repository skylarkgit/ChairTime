import sqlite3

class DataManager():
    def __init__(self):
        self.conn = sqlite3.connect("chair.db")
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS chair(presence BOOLEAN, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
        
    def setStatus(self, status: bool) -> None:
        cursor = self.conn.cursor()
        print(f'INSERT INTO chair (presence) VALUES ({status})')
        cursor.execute(f'INSERT INTO chair (presence) VALUES ({status})')
        self.conn.commit()