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
	from files import GameFiles
	files = GameFiles()
        object = files.parse_ini('graphics.ini')
        grass = GraphicEntry('grass_SEW', object.get('grass_SEW'))
	print {
		'NAME': grass.NAME,
		'TILE_X': grass.TILE_X,
		'TILE_Y': grass.TILE_Y,
		'TILE_HEIGHT': grass.TILE_HEIGHT,
		'TILE_WIDTH': grass.TILE_WIDTH,
		'COLOR_MINIMAP': grass.COLOR_MINIMAP,
		'TEXTURE_FILE': grass.TEXTURE_FILE
	}
