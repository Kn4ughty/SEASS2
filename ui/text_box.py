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


class TextBox(Element):
    """A text display ui element
    Displays text
    """
    text_colour: pg.Color
    font: str
    place_holder_text: str | None


    def __init__(self, 
        rect: pg.Rect,
        font_obj: pg.font.Font,
        text_colour: pg.Color = pg.Color(0, 0, 0),
        text_content: str = "",
        validator=lambda x: True):
        
        super().__init__(rect)
        
        self.font_obj = font_obj
        self.text_colour = text_colour
  

        self.manager = ti.TextInputManager(initial=text_content, validator=validator)
        self.visualiser = ti.TextInputVisualizer(self.manager, font_obj, font_color=text_colour)
    
    def update(self, events) -> pg.Surface:
        self.visualiser.update(events)
        return self.visualiser.surface

