import pygame as pg
import configparser

from ui.element import Element
from ui.text_display import TextDisplay

import logging
logger = logging.getLogger('root')

config = configparser.ConfigParser()

config.read('config.ini')

default_font_colour = config.get('ui', 'default_font_colour')

colour_list = default_font_colour.split(", ")
num_colour_list = []
for num in colour_list:
    num_colour_list.append(int(num))
default_font_colour = pg.Color(num_colour_list[0], num_colour_list[1], num_colour_list[2])


class Button(Element):
    """A button.
    You can click it.
    """
    text_display_obj: TextDisplay
    background_colour: pg.Color
    action: callable

    def __init__(self,
        rect: pg.Rect,
        font_obj: pg.font.Font,
        action: callable,
        background_colour: pg.Color = pg.Color(128, 128, 128), # TODO make this a config
        text_colour: pg.Color = default_font_colour,
        text_content: str = ""):

        self.rect = rect
        self.text_display_obj: TextDisplay = TextDisplay(rect, font_obj, text_colour, text_content)
        self.background_colour = background_colour
        self.action = action
    
    def update(self, mouse_pos, mouse_buttons) -> pg.Surface:
        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            self.action()

        return self.render()

    
    def render(self) -> pg.Surface:
        surface = pg.Surface((self.rect.width, self.rect.height))
        surface.fill(self.background_colour)
        surface.blit(self.text_display_obj.update(), (0, 0))
        return surface