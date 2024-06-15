from db import db
import user as user # mmm
from user import User


import user_tui

import ui

import log
logger = log.setup_custom_logger('root')
logger.debug('main message')


database = db("db.db")

cursor = database.cur


def main():
    selected_user = user_tui.looping_ui(database)



if __name__ == "__main__":
    main()
    database.con.close()
