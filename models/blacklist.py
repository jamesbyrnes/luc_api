from wrappers.sql import SqlWrapper

class Blacklist:
    TARGET_PATH = './api_data.db'

    def __init__(self):
        with SqlWrapper(Blacklist.TARGET_PATH) as db_cur:
            db_cur.execute('''CREATE TABLE IF NOT EXISTS blacklist
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                email_address TEXT NOT NULL UNIQUE);''')

    def get_all(self):
        with SqlWrapper(Blacklist.TARGET_PATH) as db_cur:
            db_cur.execute('''SELECT * FROM blacklist;''')
            return db_cur.fetchall()

    def get_by_email(self, email_address):
        with SqlWrapper(Blacklist.TARGET_PATH) as db_cur:
            db_cur.execute('''SELECT * FROM blacklist
                WHERE email_address = ?;''', [email_address])
            return db_cur.fetchone()

    def is_on_blacklist(self, email_address):
        return self.get_by_email(email_address) is not None

    def add_email(self, email_address):
        with SqlWrapper(Blacklist.TARGET_PATH) as db_cur:
            db_cur.execute('''INSERT INTO blacklist(email_address)
                VALUES (?);''', [email_address])
            last_row = db_cur.lastrowid
        return last_row
