import sqlite3

import logging

logger = logging.getLogger('root')
logger.debug('submodule message')


global path
path = "db.db"


def setPath(path: str):
    path = path


class db(object):
    con: sqlite3.Connection
    cur: sqlite3.Cursor
    
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        requiredTables = {
            "users": "uuid, name, password_hash, password_salt, creation_time",
        }

        self.initTables(requiredTables)
    

    def initTables(self, requiredTables: dict):
        tables = self.getTables()

        if type(tables) is tuple:
            logger.info("Tables found assuming all required exist")
            return

        for key in requiredTables:
            print(f"{key}({requiredTables[key]})")
            self.cur.execute(f"CREATE TABLE {key}({requiredTables[key]})")


    def getTables(self) -> tuple:
        result = self.cur.execute("SELECT name FROM sqlite_master")
        return result.fetchone()