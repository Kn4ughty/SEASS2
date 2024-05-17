import sqlite3


global path


path = "db.db"

def setPath(path: str):
    path = path


con = sqlite3.connect(path)
cur = con.cursor()

def getTables():
    res = cur.execute("SELECT name FROM sqlite_master")
    return res.fetchone()

tables = getTables()

if tables is not tuple or "users" not in tables:
    cur.execute("CREATE TABLE users(uuid, name, password_hash, password_salt)")

tables = getTables()

print(tables)


