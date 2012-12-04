import os
import re
import xml.etree.ElementTree as et

class GameFiles(object):

    GAME_DIR = None

    def find_directory(self):
        """
        Return the absolute path to the directory
        """
        if self.GAME_DIR is None:
            # TODO: Find the directory
            self.GAME_DIR = './ex'

        return os.path.abspath(self.GAME_DIR)

    def list_directory(self, dir=None):
        """
        List all files in the towns (or specified) directory
        """
        if dir is None:
            dir = self.find_directory()


        print dir
        base, dirs, files = iter(os.walk(dir)).next()

        return (base, dirs, files)

    def parse_xml(self, filename):
        """
        Return ElementTree object of the XML document
        """
        dir = self.find_directory()
        filepath = os.path.join(dir, filename)

        # Load XML into ElementTree
        tree = et.parse(filepath)
        root = tree.getroot()

        return root

    def parse_ini(self, filename):
        """
        Return object of all the entries in the ini file
        """
        entries = {}

        dir = self.find_directory()
        filepath = os.path.join(dir, filename)

        with open(filepath) as f:

            # INI parsing
            settings = re.findall(r'(\[?\w+\])?(\w+)\s?=\s?(.+)', f.read(), re.MULTILINE)

            for s in settings:
                if s[0] is not '':
                    group = s[0].strip('[]')
                else:
                    group = 'misc'

                group_entries = entries.get(group, {})
                group_entries[s[1].strip()] = s[2].strip()

                entries[group] = group_entries


            return entries


if __name__ == "__main__":
	files = GameFiles()
	print files.find_directory() 
