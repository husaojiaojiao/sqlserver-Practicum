
import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,448 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"\n修改密码\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 25, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.username.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		
		gSizer3.Add( self.username, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"姓名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.name.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		
		gSizer3.Add( self.name, 0, wx.ALL, 5 )
		
		self.m_staticText512 = wx.StaticText( self, wx.ID_ANY, u"旧密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText512.Wrap( -1 )
		self.m_staticText512.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.m_staticText512, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		self.password.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		
		gSizer3.Add( self.password, 0, wx.ALL, 5 )
		
		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"新密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )
		self.m_staticText511.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.m_staticText511, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.password1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		self.password1.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		
		gSizer3.Add( self.password1, 0, wx.ALL, 5 )
		
		self.m_staticText5111 = wx.StaticText( self, wx.ID_ANY, u"再次输入新密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5111.Wrap( -1 )
		self.m_staticText5111.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		gSizer3.Add( self.m_staticText5111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.password2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		self.password2.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		
		gSizer3.Add( self.password2, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.makesurebtn = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.makesurebtn.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.makesurebtn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.makesurebtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.makesurebtn.Bind( wx.EVT_BUTTON, self.makesure )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def makesure( self, event ):
		event.Skip()
	

