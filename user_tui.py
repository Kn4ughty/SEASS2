from dataclasses import dataclass
from typing import List
from getpass import getpass
import sqlite3

import user
from user import User

from db import db


def get_user_list_to_str(database: db) -> str:
    user_list = user.get_users_in_db(database.cur)
    out = ""
    for u in user_list:
        out += str(u.safe_str() + "\n")
    return out


def get_user_list_to_list_str(user_list: List[User]) -> List[str]:
    out = []
    for i in range(len(user_list)):
        out.append(f"#{i+1}. {user_list[i].safe_str()}")
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
    u = user.manual_init(database.cur, name, password)

    user.add_user_to_db(u, database)

    success = user.is_user_in_db(u, database)
    if success:
        print("User successfully added to the database.")
    else:
        print("Yeah so something didnt work sorry.")


def select_user_ui(database: db) -> User:
    user_list = user.get_users_in_db(database.cur)

    user_list_str = get_user_list_to_list_str(user_list)

    for entry in user_list_str:
        print(entry)

    selected_num = input("Please select user number: ")
    try:
        selected_user = user_list_str[int(selected_num) - 1]
        return user_list[int(selected_num) - 1]
    except:
        print("Invalid user number")
        return None


def login_prompt(u: User):
    print(f"Loggin in as user {u.name}")
    password = getpass("Password: ")
    return u.login(password)


def looping_ui(database: db) -> User:
    help_text = "User selection UI\n\
    p   - Print existing user\n\
    a   - Add new user\n\
    l   - Login\n\
    ?|h - Print this help menu\n\
    q   - Quit program"

    getting_input = True

    print(help_text)

    while getting_input:

        i = input("$: ")

        match i:
            case "p":

                print(get_user_list_to_str(user.get_users_in_db(database.cur)))

            case "a":
                create_user_ui(database)
            
            case "l":
                selected_user = select_user_ui(database)
                login_prompt(selected_user)

            case "?":
                print(help_text)

            case "q":
                exit()

            case "kitty cat":
                what_the_sigma()

            case _:
                print("Unknown command. Type \"?\" for list of commands.")

