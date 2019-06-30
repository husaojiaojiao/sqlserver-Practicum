

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"设备信息", pos = wx.DefaultPosition, size = wx.Size( 500,644 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"\n设备信息\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"设备编号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 20, 72, 90, 90, False, "华文隶书" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.equid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.equid.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.equid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.equid, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"申报人姓名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 20, 72, 90, 90, False, "华文隶书" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText51.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.sname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.sname.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.sname.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.sname, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"申报日期", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		self.m_staticText52.SetFont( wx.Font( 20, 72, 90, 90, False, "华文隶书" ) )
		self.m_staticText52.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText52.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.date = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.date.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.date.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.date, 0, wx.ALL, 5 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"所在实验室", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		self.m_staticText53.SetFont( wx.Font( 20, 72, 90, 90, False, "华文隶书" ) )
		self.m_staticText53.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText53.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.labid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.labid.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.labid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.labid, 0, wx.ALL, 5 )
		
		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"故障信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		self.m_staticText54.SetFont( wx.Font( 20, 72, 90, 90, False, "华文隶书" ) )
		self.m_staticText54.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText54.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.info = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.info.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.info.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.info, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.makesurebtn = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.makesurebtn.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.makesurebtn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer3.Add( self.makesurebtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.makesurebtn.Bind( wx.EVT_BUTTON, self.makesure )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def makesure( self, event ):
		event.Skip()
	

