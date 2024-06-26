import pygame as pg
import configparser

from ui.element import Element

import config_utils

import logging
logger = logging.getLogger('root')

config = configparser.ConfigParser()

config.read('config.ini')

default_font_colour = config_utils.colour_str_to_colour(config.get('ui', 'default_font_colour'))



class TextDisplay(Element):

    def __init__(self, 
        rect: pg.Rect,
        font_obj: pg.font.Font,
        text_colour: pg.Color = default_font_colour,
        text_content: str = ""):
        
        self.rect = rect # Abstraction is silly anyway.
        
        self.font_obj = font_obj
        self.text_colour = text_colour
        self.text_content = text_content
    
    def update(self) -> pg.Surface:
        return self.render()

    
    def render(self) -> pg.Surface:
        surface = self.font_obj.render(self.text_content, True, self.text_colour)
        return surface