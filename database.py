import sqlite3
from os import path

class Databases:
    def __init__(self) -> None:
        self.connect = sqlite3.connect('Info.db')
        self.execute_querry  = self.connect.cursor()
        if not path.exists('Info.db'):
            self.create_database()

    def create_database(self):
        self.execute_querry.execute(
            """
            CREATE TABLE PASSWORDLIST
            (
                CURRENT  TEXT    NOT NULL,
                NEW  TEXT    NOT NULL,
                RETYPE TEXT    NOT NULL

            );

            """
        )
        self.connect.commit()
    
    def Insert_data(self,data):
        if self.execute_querry.execute("INSERT INTO `PASSWORDLIST`(CURRENT,NEW,RETYPE) values(?,?,?)",data):
            print('OK')
            self.connect.commit()
            return True
        else:
            return False

    def __del__(self):
        self.connect.close()