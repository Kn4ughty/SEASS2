from dataclasses import dataclass
from typing import List
from getpass import getpass
import sqlite3

import user
from user import User

from db import db

global help_text
help_text = "User selection UI\
    1 - Print existing user\
    2 - Add new user\
    ? - Print this help menu\
    q - Quit program"


def user_list_to_str(user_list: List[User]) -> str:
    out = ""
    for u in user_list:
        out += str(u.safe_str() + "\n")
    return out

def what_the_sigma():
    print("kitty cat kitty cat")
    print("omg hes dancing so good")
    print("oh no whats that truck doing")
    print("its coming right for the kitty cat!!")
    print("NOOOOOOOO HE HIT HIMMMM")
    print("WAAAAHHHHHHHHHHHHH IM CRYINGGGGG")


def create_user_ui(database: db):
    name = input("Name: ")
    password = getpass("Password: ")

    u = User.manual_init(database.cur, name, password)

    user.add_user_to_db(u, database)



def user_select_ui(database: db) -> None | bool:
    

    i = input("$: ")

    match i:
        case "1":
           
            print(user_list_to_str(user.get_users_in_db(database.cur)))

        case "2":
            # add new user
            # first check if user already exisits
            create_user_ui(database)
            
        case "?":
            print(help_text)

        case "q":
            exit()

        case "kitty cat":
            what_the_sigma()
        
        case _:
            print("huh?")


def looping_ui(database: db) -> None:
    getting_input = True

    print(help_text)

    while getting_input:

        if user_select_ui(database) == False:
            getting_input = False

