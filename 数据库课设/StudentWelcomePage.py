
# -*- coding: utf-8 -*- 

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 803,645 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"\n欢迎登陆实验室设备维护管理系统\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 35, 72, 90, 92, False, "华文隶书" ) )
		
		bSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"同学你好，欢迎登陆" ), wx.VERTICAL )
		
		gSizer4 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.equipmentRepairbtn = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"设备报修", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.equipmentRepairbtn.SetFont( wx.Font( 25, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer4.Add( self.equipmentRepairbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.myRepairbtn = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"我的报修", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.myRepairbtn.SetFont( wx.Font( 25, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer4.Add( self.myRepairbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.sQuit = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"退出登陆", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.sQuit.SetFont( wx.Font( 25, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer4.Add( self.sQuit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer5.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.equipmentRepairbtn.Bind( wx.EVT_BUTTON, self.repair )
		self.myRepairbtn.Bind( wx.EVT_BUTTON, self.myRepair )
		self.sQuit.Bind( wx.EVT_BUTTON, self.quit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def repair( self, event ):
		event.Skip()
	
	def myRepair( self, event ):
		event.Skip()
	
	def quit( self, event ):
		event.Skip()
	
