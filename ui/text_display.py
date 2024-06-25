import pygame as pg
import configparser
import pygame_textinput as ti

from ui.element import Element

import logging
logger = logging.getLogger('root')

config = configparser.ConfigParser()

config.read('config.ini')

default_font = config.get('ui', 'default_font')
default_font_colour = config.get('ui', 'default_font_colour')
colour_list = default_font_colour.split(", ")
num_colour_list = []
for num in colour_list:
    num_colour_list.append(int(num))
default_font_colour = pg.Color(num_colour_list[0], num_colour_list[1], num_colour_list[2])


class TextDisplay(Element):

    def __init__(rect: pg.Rect,
        font_obj: pg.font.Font,
        text_colour: pg.Color = pg.Color(0, 0, 0),
        text_content: str = ""):
        
        super().__init__(pg.Rect(rect))
        
        self.font_obj = font_obj
        self.text_colour = text_colour