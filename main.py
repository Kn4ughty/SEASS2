from db import db
import User as user # mmm
from User import User

import ui

import log
logger = log.setup_custom_logger('root')
logger.debug('main message')

database = db("db.db")

cursor = database.cur


def main():
    u = User("UUID", "A name", "SOME PASSWORD HASH", "SALT", 1234.5)
 
    user.add_user_to_db(u, database)

    print(user.get_users_in_db(cursor))


if __name__ == "__main__":
    main()
    database.con.close()
