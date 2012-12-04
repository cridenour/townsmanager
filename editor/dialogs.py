import wx

def AboutDialog(frame):
    dlg = wx.MessageDialog(frame, u"Towns Manager v0.1, \xa9 Chris Ridenour", "About Towns Manager", wx.OK)
    dlg.ShowModal()
    dlg.Destroy()