import sqlite3

import logging

logger = logging.getLogger('root')
logger.debug('submodule message')


global path
path = "db.db"


def setPath(path: str):
    path = path


class db(object):
    cur: sqlite3.Cursor
    
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        requiredTables = {
            "users": "uuid, name, password_hash, password_salt, creation_date",
        }

        self.initTables(requiredTables)

        print(self.getTables())
    

    def initTables(self, requiredTables: dict):
        tables = self.getTables()
        print(type(tables))

        if type(tables) is tuple:
            logger.info("Tables found assuming all required exist")
            return

        for key in requiredTables:
            print("DOING SHIT")
            print(f"{key}({requiredTables[key]})")
            self.cur.execute(f"CREATE TABLE {key}({requiredTables[key]})")


    def getTables(self) -> tuple:
        result = self.cur.execute("SELECT name FROM sqlite_master")
        return result.fetchone()


    def sendCommand(self, command: str) -> sqlite3.Cursor:
        """
        ASUMES COMAND IS SAFE
        """
        result = self.cur.execute(command)
        return result


