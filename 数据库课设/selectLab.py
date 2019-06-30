

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"实验室查询", pos = wx.DefaultPosition, size = wx.Size( 500,384 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"\n实验室查询\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		self.m_staticText37.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText37.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText37.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer4.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"实验室编号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		self.m_staticText39.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText39.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText39.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer4.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.labid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.labid.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.labid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer4.Add( self.labid, 0, wx.ALL, 5 )
		
		self.m_staticText391 = wx.StaticText( self, wx.ID_ANY, u"实验室设备总台数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )
		self.m_staticText391.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText391.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText391.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer4.Add( self.m_staticText391, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.totalNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.totalNum.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.totalNum.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer4.Add( self.totalNum, 0, wx.ALL, 5 )
		
		self.m_staticText392 = wx.StaticText( self, wx.ID_ANY, u"设备损坏台数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText392.Wrap( -1 )
		self.m_staticText392.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText392.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText392.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer4.Add( self.m_staticText392, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.faultNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.faultNum.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.faultNum.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer4.Add( self.faultNum, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.selectLab = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.selectLab.SetFont( wx.Font( 20, 72, 90, 90, False, "华文隶书" ) )
		self.selectLab.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer4.Add( self.selectLab, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.selectLab.Bind( wx.EVT_BUTTON, self.select )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def select( self, event ):
		event.Skip()
	

