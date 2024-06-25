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


class TextEntry(Element):
    """A text typing box.
    You can type text into it.
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
        
        super().__init__(pg.Rect(rect))
        
        self.font_obj = font_obj
        self.text_colour = text_colour
  
        self.manager = ti.TextInputManager(initial=text_content, validator=validator)
        self.visualiser = ti.TextInputVisualizer(self.manager, font_obj, font_color=text_colour)

        self._selected = False
        self._surface: pg.Surface = pg.Surface((self.rect.width, self.rect.height))


    def update(self, events) -> pg.Surface:
        if self._selected:
            self.visualiser.update(events)

        self._render()
        print(self.manager.value)
        
        return self._surface

    def _render(self):

        if self._selected:
            self.visualiser.cursor_visible = True
        else:
            self.visualiser.cursor_visible = False

        self._surface.fill(pg.Color(255, 255, 255))
        self._surface.blit(self.visualiser.surface, (0, 0))


    @property
    def selected(self) -> bool:
        return self._selected


    @selected.setter
    def selected(self, value: bool):
        self._selected = value