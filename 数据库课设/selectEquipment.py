
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"设备查询", pos = wx.DefaultPosition, size = wx.Size( 500,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"\n设备查询\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		self.m_staticText28.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText28.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"设备编号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText29.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.equid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.equid.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.equid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.equid, 0, wx.ALL, 5 )
		
		self.m_staticText291 = wx.StaticText( self, wx.ID_ANY, u"所在实验室", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )
		self.m_staticText291.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText291.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText291.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText291, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.labid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.labid.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.labid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.labid, 0, wx.ALL, 5 )
		
		self.m_staticText292 = wx.StaticText( self, wx.ID_ANY, u"使用状态", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText292.Wrap( -1 )
		self.m_staticText292.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText292.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText292.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText292, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.statues = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.statues.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.statues.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.statues, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.selectbtn = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.selectbtn.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.selectbtn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3.Add( self.selectbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.selectbtn.Bind( wx.EVT_BUTTON, self.select )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def select( self, event ):
		event.Skip()
	

