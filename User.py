from dataclasses import dataclass
from typing import List
import time
import sqlite3

from db import db # mmm confusing
#from db import db

import logging

logger = logging.getLogger('root')
logger.debug('submodule message')


@dataclass
class User:
    uuid: str
    name: str
    password_hash: str
    password_salt: str
    creation_date: float


def add_user_to_db(user: User, database: db) -> Exception | None:
    logger.info(f"Adding user ({user}) to database")

    all_users = get_users_in_db(database.cur)

    for instance in all_users:
        if instance.uuid == user.uuid:
            logger.info("User is already found in DB")
            raise IOError("User was already found in the database!!!!!!!!!!!!")


    logger.debug("Executing SQL")
    database.cur.execute(""" 
    INSERT INTO "users"("uuid","name","password_hash","password_salt", creation_date)
    VALUES( 
        :uuid,
        :name,
        :password_hash,
        :password_salt,
        :creation_date)""",
    {
        'uuid': user.uuid,
        'name': user.name, 
        'password_hash': user.password_hash,
        'password_salt': user.password_salt,
        'creation_date': user.creation_date
    })

    database.con.commit()


def get_users_in_db(cursor: sqlite3.Cursor) -> List[User]:
    logger.debug(f"getting users in db")

    result = cursor.execute("SELECT * FROM users LIMIT 100").fetchall()

    logger.debug(f"Users found in DB. raw result: {result}")

    user_list = []

    for user_tuple in result:
        u = User(user_tuple[0], user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4])
        user_list.append(u)
    
    logger.debug(f"Users found in DB. turned to User type: {user_list}")


    return user_list


database = db("db.db")

get_users_in_db(database.cur)



