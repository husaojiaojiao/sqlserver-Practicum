
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 963,687 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"\n欢迎登陆实验室设备维护管理系统\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 35, 72, 90, 92, False, "华文隶书" ) )
		
		bSizer4.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"老师你好，欢迎登陆" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.fix = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"设备维修", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		self.fix.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer2.Add( self.fix, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.manage = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"设备管理", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		self.manage.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer2.Add( self.manage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.selectEqu = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"设备查询", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		self.selectEqu.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer2.Add( self.selectEqu, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.selectLabbtn = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"实验室查询", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		self.selectLabbtn.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer2.Add( self.selectLabbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.log = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"维修日志", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		self.log.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer2.Add( self.log, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.tQuit = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"退出登陆", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		self.tQuit.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer2.Add( self.tQuit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.fix.Bind( wx.EVT_BUTTON, self.fixEquipment )
		self.manage.Bind( wx.EVT_BUTTON, self.manageEquipment )
		self.selectEqu.Bind( wx.EVT_BUTTON, self.selectEquipment )
		self.selectLabbtn.Bind( wx.EVT_BUTTON, self.selectLab )
		self.log.Bind( wx.EVT_BUTTON, self.fixLog )
		self.tQuit.Bind( wx.EVT_BUTTON, self.teacherQuit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def fixEquipment( self, event ):
		event.Skip()
	
	def manageEquipment( self, event ):
		event.Skip()
	
	def selectEquipment( self, event ):
		event.Skip()
	
	def selectLab( self, event ):
		event.Skip()
	
	def fixLog( self, event ):
		event.Skip()
	
	def teacherQuit( self, event ):
		event.Skip()
	

