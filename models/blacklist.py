import sqlite3

class Blacklist:
    TARGET_PATH = './api_data.db'

    def __init__(self):
        with sqlite3.connect(Blacklist.TARGET_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                email_address TEXT NOT NULL UNIQUE);''')
            conn.commit()

    def get_all(self):
        with sqlite3.connect(Blacklist.TARGET_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM blacklist;''')
            return cursor.fetchall()

    def get_by_email(self, email_address):
        with sqlite3.connect(Blacklist.TARGET_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM blacklist
                WHERE email_address = ?;''', [email_address])
            return cursor.fetchone()

    def is_on_blacklist(self, email_address):
        return self.get_by_email(email_address) is not None

    def add_email(self, email_address):
        with sqlite3.connect(Blacklist.TARGET_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO blacklist(email_address)
                VALUES (?);''', [email_address])
            last_row = cursor.lastrowid
            conn.commit()

        return last_row
