# -*- coding: utf-8 -*-
# @Author: yezhipeng
# @Date:   2019-05-27 16:16:32
# @Last Modified by:   yezhipeng
# @Last Modified time: 2019-05-27 17:43:54
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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent, equipmentlist ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,473 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"\n设备报修\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText29.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer2.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"设备编号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		# equidChoices = []
		self.equid = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), equipmentlist, 0 )
		self.equid.SetSelection( 0 )
		self.equid.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.equid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.equid, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"故障信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer3.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.faultInfo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,100 ), wx.TE_MULTILINE )
		self.faultInfo.SetFont( wx.Font( 15, 72, 90, 92, False, "黑体" ) )
		self.faultInfo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		gSizer3.Add( self.faultInfo, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		self.makeSurebtn = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.makeSurebtn.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		self.makeSurebtn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer2.Add( self.makeSurebtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.equid.Bind( wx.EVT_CHOICE, self.onChoice )
		self.makeSurebtn.Bind( wx.EVT_BUTTON, self.makeSure )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onChoice( self, event ):
		event.Skip()
	
	def makeSure( self, event ):
		event.Skip()
	

