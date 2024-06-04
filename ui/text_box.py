import pygame as pg
import configparser

from element import Element

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


class Text(Element):
    """A text display ui element
    Displays text
    """
    text_colour: pg.Color
    font: str
    place_holder_text: str | None


    def __init__(self, 
        element: Element,
        text_content: str = "",
        font_size: int = None,
        font: str = default_font,
        text_colour: pg.Color = pg.Color(0, 0, 0),
        place_holder_text: str = ""):
        
        self.element = Element(element)
        
        self.font_size = font_size
        self.font = default_font
        self.text_colour = text_colour
        self.place_holder_text = place_holder_text
