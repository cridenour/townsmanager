import wx
from editor.dialogs import *
from editor.panels import *

class MainFrame(wx.Frame):
    """
    Our main frame for the application
    """
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Towns Manager", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.Size( 800,600 ), wx.Size( 800,600 ) )

        gSizer1 = wx.GridSizer( 2, 2, 0, 0 )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour((255,255,255))
        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"./editor/graphics/logo_square.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 20 )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Play Towns", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 18, 70, 90, 91, False, "Helvetica" ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

        self.m_panel1.SetSizer( bSizer1 )
        self.m_panel1.Layout()
        bSizer1.Fit( self.m_panel1 )
        gSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap11 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"./editor/graphics/gears_square.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_bitmap11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 20 )

        self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Play Towns", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetFont( wx.Font( 18, 70, 90, 91, False, "Helvetica" ) )

        bSizer11.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

        self.m_panel2.SetSizer( bSizer11 )
        self.m_panel2.Layout()
        bSizer11.Fit( self.m_panel2 )
        gSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap12 = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.Bitmap( u"./editor/graphics/logo_square.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_bitmap12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 20 )

        self.m_staticText12 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Play Towns", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetFont( wx.Font( 18, 70, 90, 91, False, "Helvetica" ) )

        bSizer12.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

        self.m_panel3.SetSizer( bSizer12 )
        self.m_panel3.Layout()
        bSizer12.Fit( self.m_panel3 )
        gSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap13 = wx.StaticBitmap( self.m_panel4, wx.ID_ANY, wx.Bitmap( u"./editor/graphics/logo_square.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_bitmap13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 20 )

        self.m_staticText13 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Play Towns", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        self.m_staticText13.SetFont( wx.Font( 18, 70, 90, 91, False, "Helvetica" ) )

        bSizer13.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )

        self.m_panel4.SetSizer( bSizer13 )
        self.m_panel4.Layout()
        bSizer13.Fit( self.m_panel4 )
        gSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_panel1.Bind( wx.EVT_ENTER_WINDOW, self.EnterPlayPanel )
        self.m_panel1.Bind( wx.EVT_LEAVE_WINDOW, self.LeavePlayPanel )


        # Set up the menu
        file = wx.Menu()

        about = file.Append(wx.ID_ABOUT, "About Towns Manager")
        file.AppendSeparator()
        exit = file.Append(wx.ID_EXIT,"Exit")

        # Add the bindings
        self.Bind(wx.EVT_MENU, lambda event: AboutDialog(self), about)
        self.Bind(wx.EVT_MENU, lambda event: self.Close(), exit)

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(file,"&File")
        self.SetMenuBar(menuBar)


        self.Show(True)

    def EnterPlayPanel(self, event):
        sender = event.GetEventObject()
        sender.SetBackgroundColour((130,130,130))
        sender.Refresh()

    def LeavePlayPanel(self, event):
        sender = event.GetEventObject()
        sender.SetBackgroundColour((255,255,255))
        sender.Refresh()