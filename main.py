import wx
from editor.frames import *

if __name__=="__main__":
    app = wx.App(False)
    frame = MainFrame(None)
    app.MainLoop()