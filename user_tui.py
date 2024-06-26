from dataclasses import dataclass
from typing import List
from getpass import getpass
import sqlite3
import sys

import user
from user import User

from db import db


def get_user_list_to_str(user_list: List[User]) -> str:
    out = ""
    for i in range(len(user_list)):
        out += (f"\n#{i+1}. {user_list[i].safe_str()}")
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
    print("")
    for entry in user_list_str:
        print(entry)
    print("")

    selected_num = input("Please enter user number: ")
    try:
        selected_user = user_list_str[int(selected_num) - 1]
        return user_list[int(selected_num) - 1]
    except:
        print("Invalid user number")
        raise ValueError("Invalid user number")


def login_prompt(u: User) -> bool:
    print(f"Loggin in as user \"{u.name}\"")
    password = getpass("Password: ")
    return u.login(password)


def parse_args(args: List[str]) -> str:
    args.pop(0) # Remove file name
    
    return args[0]


def looping_ui(database: db) -> User:
    help_text = "Available commands:\n\
    ls   - List existing users\n\
    a   - Add new user (ONLY ADMIN USER CAN ACCESS PROGRAM) \n\
    l   - Login\n\
    ?|h - Print this help menu\n\
    q   - Quit program"

    getting_input = True

    print(help_text)
    args = sys.argv
    print(len(args))

    while getting_input:
        
        if len(args) <= 1:
            i = input("$: ")
        else:
            i = parse_args(args)

        match i:
            case "ls":

                user_list = get_user_list_to_str(user.get_users_in_db(database.cur))
                if user_list == "":
                    print("No users found in database")
                    print("Consider creating one with the \"a\" command")
                else:
                    print(user_list)

            case "a":
                create_user_ui(database)
            
            case "l":
                try:
                    selected_user = select_user_ui(database)
                except ValueError:
                    continue

                is_logged_in = login_prompt(selected_user)
                if is_logged_in:
                    return selected_user
                else:
                    print("Login failed")

            case "?":
                print(help_text)

            case "q":
                exit()

            case "kitty cat":
                what_the_sigma()

            case _:
                print("Unknown command. Type \"?\" for list of commands.")


