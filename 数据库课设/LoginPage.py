
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"实验室设备维护管理系统", pos = wx.DefaultPosition, size = wx.Size( 500,354 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetExtraStyle( wx.FRAME_EX_CONTEXTHELP )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 94, 91, False, "@微软雅黑" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"\n用户登陆", wx.DefaultPosition, wx.Size( -1,120 ), wx.ALIGN_CENTRE )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 30, 73, 90, 92, False, "华文隶书" ) )
		self.title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 3, 2, 0, 0 )
		
		self.username = wx.StaticText( self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTRE )
		self.username.Wrap( -1 )
		self.username.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.username.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.username.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer1.Add( self.username, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.inputUnm = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.inputUnm.SetFont( wx.Font( 13, 72, 90, 92, False, "微软雅黑" ) )
		self.inputUnm.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.inputUnm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.password = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTRE )
		self.password.Wrap( -1 )
		self.password.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.password.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.password.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer1.Add( self.password, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.inputPwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), wx.TE_PASSWORD )
		self.inputPwd.SetFont( wx.Font( 13, 72, 90, 92, False, "微软雅黑" ) )
		self.inputPwd.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer1.Add( self.inputPwd, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.loginbtn = wx.Button( self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.loginbtn.SetFont( wx.Font( 15, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.loginbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.registerbtn = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.registerbtn.SetFont( wx.Font( 15, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.registerbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.forgetbtn = wx.Button( self, wx.ID_ANY, u"忘记密码", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.forgetbtn.SetFont( wx.Font( 15, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.forgetbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.changebtn = wx.Button( self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.changebtn.SetFont( wx.Font( 15, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.changebtn, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.loginbtn.Bind( wx.EVT_BUTTON, self.login )
		self.registerbtn.Bind( wx.EVT_BUTTON, self.register )
		self.forgetbtn.Bind( wx.EVT_BUTTON, self.forget )
		self.changebtn.Bind( wx.EVT_BUTTON, self.change )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()
	
	def register( self, event ):
		event.Skip()
	
	def forget( self, event ):
		event.Skip()
	
	def change( self, event ):
		event.Skip()
	

