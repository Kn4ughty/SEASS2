import pygame as pg

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

pg.init()

font = pg.font.SysFont(default_font, 40)



database = db("db.db")

cursor = database.cur

ui_elements = []

text_box = ui.text_box.TextBox((10, 10, 200, 50), font)
ui_elements.append(text_box)

WINDOW = pg.display.set_mode((1000, 200))
CLOCK = pg.time.Clock()

pg.key.set_repeat(200, 25)

def main():
    #selected_user = user_tui.looping_ui(database)

    while True:
        WINDOW.fill((225, 225, 225))

        events = pg.event.get()

        for element in ui_elements:
            if type(element) == ui.text_box.TextBox:
                WINDOW.blit(element.update(events), element.rect)
        

        for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
        
        pg.display.update()
        CLOCK.tick(30)



if __name__ == "__main__":
    main()
    database.con.close()
