from dataclasses import dataclass
from typing import List
import time
import sqlite3
import uuid

import bcrypt

from db import db # mmm confusing

import logging

logger = logging.getLogger('root')
logger.debug('submodule message')

class DuplicateUserError(Exception):
    pass

@dataclass
class User:
    uuid: str
    name: str
    password_hash: str
    password_salt: str
    creation_time: float


    def safe_str(self) -> str:
        out = (f"Name: {self.name:<20} Creation Time: {time.ctime(self.creation_time):<12}")
        return out
    
    def login(self, password: str) -> bool:
        logger.debug("Logging in user")
        
        password_bytes = password.encode('utf-8')
        hashed_input = bcrypt.hashpw(password_bytes, self.password_salt.encode('utf-8'))
        
        logger.debug(f"Hashed input: {hashed_input}")

        status = hashed_input == self.password_hash.encode('utf-8')
        logger.debug(f"Status: {status}")
        return status



def add_user_to_db(user: User, database: db) -> Exception | None:
    logger.info(f"Adding user ({user}) to database")

    all_users = get_users_in_db(database.cur)

    for instance in all_users:
        if instance.uuid == user.uuid:
            logger.info("User is already found in DB")
            raise DuplicateUserError("User is already in DB")


    logger.debug("Executing SQL")
    database.cur.execute(""" 
    INSERT INTO "users"("uuid","name","password_hash","password_salt", creation_time)
    VALUES( 
        :uuid,
        :name,
        :password_hash,
        :password_salt,
        :creation_time)""",
    {
        'uuid': user.uuid,
        'name': user.name, 
        'password_hash': user.password_hash,
        'password_salt': user.password_salt,
        'creation_time': user.creation_time
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


def is_user_in_db(U: User, database: db):
    user_list = get_users_in_db(database.cur)

    return True if U in user_list else False



def manual_init(cur: sqlite3.Cursor, name: str, password: str): # TODO. Give better name
    UUID = uuid.uuid4()

    user_list = get_users_in_db(cur)
    for db_user in user_list:
        if db_user.uuid == str(UUID):
            print("Wow you just got the same UUID as someone else.")
            print("This is actually insane")
            print("why did i even write this error message this will never happen")
            print("Anyway here are the errors")
            logger.info("duplicate UUID??")
            UUID = uuid.uuid4()


    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    salt_str = salt.decode('utf-8')

    hashed = bcrypt.hashpw(password_bytes, salt)
    hashed_str = hashed.decode('utf-8')


    creation_time = time.time()


    return User(str(UUID), str(name), hashed_str, salt_str, creation_time)




b = User("UUID", "A name", "SOME PASSWORD HASH", "SALT", 1234.5)
print(b.safe_str())

