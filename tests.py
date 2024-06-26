import unittest
import pygame as pg
import configparser

import config_utils as cu

config = configparser.ConfigParser()

config.read('config.ini')

class configUtilsTests(unittest.TestCase):
    
    def test_config_read(self):
        """ 
        Checks that the config file can be read
        """

        self.assertEqual(config.get("general", "DONT_CHANGE_test_value"), "test")

    def test_colour_str_to_colour(self):
        self.assertEqual(cu.colour_str_to_colour("128, 128, 128"), pg.Color(128, 128, 128))


if __name__ == '__main__':
    unittest.main()