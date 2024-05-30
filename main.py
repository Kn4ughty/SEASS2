from db import db
import User as user # mmm
from User import User

import log
logger = log.setup_custom_logger('root')
logger.debug('main message')

database = db("db.db")

cursor = database.cur


def main():
    print("Hello World")
    #print(User.get_users_in_db(cursor))
    u = User("UUIDPoop", "naeme", "SOME HASH", "SALT", 1234.5)
    print(user.add_user_to_db(u, database))
    print(user.get_users_in_db(cursor))


if __name__ == "__main__":
    main()
    database.con.close()