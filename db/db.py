import sqlite3


global path


path = "db.db"

def setPath(path: str):
    path = path


class db(object):
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

        self.requiredTables = {
            "users": "uuid, name, password_hash, password_salt",
        }

        self.initTables(self.getTables())

        print(self.getTables())
    

    def initTables(self, tables):
        if tables is not tuple:
            # LOG
            for key in self.requiredTables:
                print(f"{key}({self.requiredTables[key]})")
                self.cur.execute(f"CREATE TABLE {key}({self.requiredTables[key]})")


    def getTables(self):
        result = self.cur.execute("SELECT name FROM sqlite_master")
        return result.fetchone()
    
    def sendCommand(self, command: str) -> sqlite3.Cursor:
        """
        ASUMES COMAND IS SAFE
        """
        result = self.cur.execute(command)
        return result

a = db(path)


