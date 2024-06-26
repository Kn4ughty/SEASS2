import pygame as pg

# Not the best file name i know

def colour_str_to_colour(string: str) -> pg.Color:
    colour_list = string.split(", ")
    num_colour_list = []
    for num in colour_list:
        num_colour_list.append(int(num))
    out = pg.Color(num_colour_list[0], num_colour_list[1], num_colour_list[2])
    return out

