import pygame as pg
import os
from typing import List
import time

from db import db
import user as user # mmm
from user import User

import user_tui

import ui

import configparser
import log
logger = log.setup_custom_logger('root')
logger.debug('main message')


config = configparser.ConfigParser()
config.read('config.ini')

window_width = int(config.get('general', 'window_width'))
window_height = int(config.get('general', 'window_height'))

default_font = config.get('ui', 'default_font')
default_font_colour = config.get('ui', 'default_font_colour')


colour_list = default_font_colour.split(", ")
num_colour_list = []
for num in colour_list:
    num_colour_list.append(int(num))
default_font_colour = pg.Color(num_colour_list[0], num_colour_list[1], num_colour_list[2])

end_amount = int(config.get('game', 'ends'))
shots_per_end = int(config.get('game', 'shots_per_end'))

pg.init()

font = pg.font.Font(os.path.join("font", default_font), 25)

database = db("db.db")


CLOCK = pg.time.Clock()

pg.key.set_repeat(200, 25)

def print_hello():
    print("Hello")

def generate_score_grid(ends, shots_per_end) -> list[ui.element.Element]:
    elements = []
    for r in range(ends):
        for c in range(shots_per_end):
            box = ui.text_box.TextEntry((20 + c * 53, 100 + r * 50, 50, 30), font, validator=lambda x: x.isdigit() or x == "")
            elements.append(box)
    
    return elements


def select_next_element(elements, delta: int) -> None:
    for i in range(len(elements)):
        try:
            elements[i].selected
        except AttributeError:
            pass
        if elements[i].selected:

            elements[i].selected = False

            if i == len(elements) - 1:
                elements[0].selected = True
            else:
                elements[i + delta].selected = True

            break


def find_elements_of_type_in_list(elements: list, ty: type) -> list:
    out = []
    for element in elements:
        if type(element) == ty:
            out.append(element)
    return out


def write_scores_from_ui_elements() -> None:
    global ui_elements
    elements = ui_elements
    
    global end_amount
    rows = end_amount

    global shots_per_end
    collumns = shots_per_end

    logger.debug(f"Getting scores from ui elements")
    text_elements = find_elements_of_type_in_list(elements, ui.text_box.TextEntry)

    scores = []
    if rows * collumns != len(text_elements):
        raise ValueError("Error getting scores from list. Length of list does not match rows and collumns")
    
    for i in range(rows):
        scores.append([])
        for j in range(collumns):
            chosen = elements[i * collumns + j]
            assert type(chosen) == ui.text_box.TextEntry 
            text = chosen.text_content
            if text == "":
                scores[i].append(0)
            else:
                scores[i].append(int(chosen.text_content))
            
    logger.debug(f"Scores extracted = {scores}")

    csv = list_to_csv_str(scores)

    s = time.strftime("%Y-%m-%d__%H:%M:%S", time.localtime())
    print(s)
    path = os.path.join("exported", f"{s}.csv")

    try:
        with open(path, "x") as f:
            f.write(csv)
    
    except FileExistsError:
        logger.warn("File already found. Perhapse you pressed submit in quick sucession.")


def list_to_csv_str(lst: List) -> str:
    out = ""
    for row in lst:
        line = ""
        for j in range(len(row)):
            item = row[j]

            if j == len(row) - 1:
                line += f"{str(item)}"
            else:
                line += f"{str(item)},"

        out += f"{line}\n"

    return out


def main():
    selected_user = user_tui.looping_ui(database)

    if selected_user.uuid != "ad1a0aba-24b0-45d5-bc47-f40f9f82e2e6":
        print("WRONG USER!!!\n"*5)
        print("You must log in as the admin to access the program!")
        exit()

    global ui_elements
    ui_elements = []

    for element in generate_score_grid(end_amount, shots_per_end):
        ui_elements.append(element)

    ui_elements[0].selected = True

    ui_elements.append(ui.text_display.TextDisplay(pg.Rect(10, 10, 10, 10), font, text_content="󱡁 Enter score into grid"))

    ui_elements.append(
        ui.button.Button(pg.Rect(10, 700, 200, 50), 
        font, write_scores_from_ui_elements, text_content="󰈇 Export data"))

    print(ui_elements[-1].text_display_obj.text_content)

    WINDOW = pg.display.set_mode((window_width, window_height))

    while True:
        WINDOW.fill((128, 128, 128))


        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            # If tab pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    select_next_element(ui_elements, 1)
            

        mouse_pos = pg.mouse.get_pos()
        mouse_just_released = pg.mouse.get_just_released()
        
        for element in ui_elements:
            if type(element) == ui.text_box.TextEntry:
                WINDOW.blit(element.update(events), element.rect)

            elif type(element) == ui.button.Button:
                WINDOW.blit(element.update(mouse_pos, mouse_just_released), element.rect)

            else:
                WINDOW.blit(element.update(), element.rect)


        pg.display.update()
        CLOCK.tick(30)



if __name__ == "__main__":
    main()
    database.con.close()
