import os
import re
import xml.etree.ElementTree as et

class GraphicEntry(object):

    NAME = None
    TILE_X = None
    TILE_Y = None
    TILE_HEIGHT = None
    TILE_WIDTH = None
    COLOR_MINIMAP = None
    TEXTURE_FILE = None

    def __init__(self, name, inigroup):
        self.NAME = name
        # Get the other attributes we have
        for key, val in inigroup.items():
            self.__setattr__(key, val)

if __name__ == "__main__":
	pass
