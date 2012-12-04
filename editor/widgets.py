import wx

class EditableTextCtrl(wx.TextCtrl):
    _reference = None

    def __init__(self, ref, *args, **kwargs):
        wx.TextCtrl.__init__(*args, **kwargs)
        # Set our reference
        self._reference = ref