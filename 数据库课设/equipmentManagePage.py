

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent, labChoiceChoices ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"设备管理", pos = wx.DefaultPosition, size = wx.Size( 594,424 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"\n管理设备\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer2.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"未修复总数量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer2.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.numOfFault = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.numOfFault.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.numOfFault.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer2.Add( self.numOfFault, 0, wx.ALL, 5 )
		
		self.m_staticText201 = wx.StaticText( self, wx.ID_ANY, u"实验室", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )
		self.m_staticText201.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText201.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText201.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer2.Add( self.m_staticText201, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		# labChoiceChoices = []
		self.labChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), labChoiceChoices, 0 )
		self.labChoice.SetSelection( 0 )
		self.labChoice.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.labChoice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer2.Add( self.labChoice, 0, wx.ALL, 5 )
		
		self.m_staticText2011 = wx.StaticText( self, wx.ID_ANY, u"此实验室未修复数量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2011.Wrap( -1 )
		self.m_staticText2011.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText2011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText2011.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer2.Add( self.m_staticText2011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.numOfTheLab = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.numOfTheLab.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.numOfTheLab.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer2.Add( self.numOfTheLab, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.labChoice.Bind( wx.EVT_CHOICE, self.OnChoice )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChoice( self, event ):
		event.Skip()
	

