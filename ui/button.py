import pygame as pg
import configparser

from ui.element import Element
from ui.text_display import TextDisplay

import config_utils

import logging
logger = logging.getLogger('root')

config = configparser.ConfigParser()

config.read('config.ini')

default_font_colour = config_utils.colour_str_to_colour(config.get('ui', 'default_font_colour'))
default_background_colour = config_utils.colour_str_to_colour(config.get('ui', 'default_background_colour'))



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
        background_colour: pg.Color = default_background_colour,
        text_colour: pg.Color = default_font_colour,
        text_content: str = ""):

        self.rect = rect
        self.text_display_obj: TextDisplay = TextDisplay(rect, font_obj, text_colour, text_content)
        self.background_colour = background_colour
        self.action = action
    
    def update(self, mouse_pos, mouse_buttons) -> pg.Surface:
        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            print("Clicked")
            self.action()

        return self.render()

    
    def render(self) -> pg.Surface:
        surface = pg.Surface((self.rect.width, self.rect.height))
        surface.fill(self.background_colour)
        surface.blit(self.text_display_obj.update(), (0, 0))
        return surface