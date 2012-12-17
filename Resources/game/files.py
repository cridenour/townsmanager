import os
import re
import codecs
import shutil
import subprocess
try:
    import lxml.etree as et
except ImportError:
    import xml.etree.ElementTree as et

class GameFiles(object):
    """
    Class for handling the generic file handling operations.
    """

    GAME_DIR = None

    # A few generic locations the directory might be in.
    USUAL_LOCATIONS = [
        '~/Library/Application Support/Steam/SteamApps/common/towns',
        'C:/Program Files (x86)/Steam/steamapps/common/towns',
        'C:/Program Files/Steam/steamapps/commmon/towns',
        '/Applications/Towns',
	'~/Applications/Towns'
    ]

    def find_directory(self):
        """
        Return the absolute path to the directory
        """
        if self.GAME_DIR is None:
            for loc in self.USUAL_LOCATIONS:
                if os.path.exists(os.path.expanduser(loc)):
                    self.GAME_DIR = os.path.abspath(os.path.expanduser(loc))

        # If we still don't find it, set it to false so our UI can prompt
        if self.GAME_DIR is None:
            self.GAME_DIR = False

        return self.GAME_DIR

    def launch_towns(self):
        """
        Launch the game
        """
        osx = os.path.join(self.find_directory(), 'towns.command')
        win = os.path.join(self.find_directory(), 'Towns.exe')
        linux = os.path.join(self.find_directory(), 'towns.sh')

        if os.path.exists(win):
            subprocess.Popen('"' + win + '"', cwd=self.find_directory(), shell=True)
        elif os.path.exists(osx):
            subprocess.Popen('"' + osx + '"', cwd=self.find_directory(), shell=True)
	elif os.path.exists(linux):
	    subprocess.Popen('"' + linux + '"', cwd=self.find_directory(), shell=True)

    def list_directory(self, dir=None):
        """
        List all files in the towns (or specified) directory
        """
        if dir is None:
            # Assume they want the full directory tree
            dir = self.find_directory()

        else:
            # Assume the directory is relative
            dir = os.path.join(self.find_directory(), dir)

        base, dirs, files = iter(os.walk(dir)).next()

        # OSX: Remove .DS_Store files
        try:
            files.remove('.DS_Store')
        except ValueError:
            pass

        return base, dirs, files

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

    def indent_xml(self, elem, level=0):
        i = "\n" + level*"\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent_xml(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i


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

    def save_xml(self, filename, et_obj):
        """
        Takes an element tree object and writes a new XML file based on it.
        """

        content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        try:
            content += et.tostring(et_obj, pretty_print=True, encoding='utf-8')
        except TypeError:
            content += et.tostring(et_obj, encoding='utf-8')

        # Change to windows line endings to further mirror the original file.
        content = re.sub("\r(?!\n)|(?<!\r)\n", "\r\n", content)

        dir = self.find_directory()
        filepath = os.path.join(dir, filename)

        with open(filepath, 'w') as f:
            f.write(codecs.BOM_UTF8)
            f.write(content)

    def copy_folder(self, source, destination):
        """
        Copies a folder source to a destination. Destination will be the new name of the folder, relative to root
        """

        if not os.path.exists(os.path.join(self.find_directory(), destination)):
            if os.path.exists(os.path.join(self.find_directory(), source)):
                shutil.copytree(os.path.join(self.find_directory(), source), os.path.join(self.find_directory(), destination))
        else:
            raise OSError

    def delete_folder(self, folder):
        """
        Deletes a folder relative to the root
        """
        shutil.rmtree(folder)


if __name__ == "__main__":
	files = GameFiles()
	print files.find_directory() 

	graphics = files.parse_ini('graphics.ini')
	print '%s Graphic entries' % len(graphics)
