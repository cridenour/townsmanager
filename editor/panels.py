import os
import wx
from game.files import GameFiles
from game.objects import GraphicEntry

class TownsDirList(wx.Panel):
    """
    Lists all the files in your towns directory
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.control = wx.TreeCtrl(self, size=(200,400))
        self.files = GameFiles()

        root = self.control.AddRoot('Towns')

        # Start our recursion fun
        self.add_file_tree_items(root, None)

        self.control.Expand(root)

    def add_file_tree_items(self, parent, dir):
        """
        A recursive loop for walking the directories and files
        """

        base, dirs, files =  self.files.list_directory(dir)

        for d in dirs:
            id = self.control.AppendItem(parent, d)
            self.add_file_tree_items(id, os.path.join(base, d))

        for f in files:
            self.control.AppendItem(parent, f)


class GraphicsEditor(wx.Panel):
    """
    The panel for editing the graphics.ini file
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(800,600))

        self.files = GameFiles()
        self.object = self.files.parse_ini(os.path.join(self.files.find_directory(), 'graphics.ini'))

        grass = GraphicEntry('grass', self.object.get('grass'))

        groups_sizer = wx.BoxSizer(wx.HORIZONTAL)
        groups_sizer.Add(wx.StaticText(self, label='Tile Height: ', style=wx.ALIGN_RIGHT, size=(80,20)))
        grass_height = wx.TextCtrl(self, style=wx.ALIGN_LEFT, size=(80,20))
        grass_height.AppendText(grass.TILE_HEIGHT)
        flags = wx.SizerFlags(1)
        flags.Bottom()
        groups_sizer.AddF(grass_height, flags)

        self.SetSizer(groups_sizer)