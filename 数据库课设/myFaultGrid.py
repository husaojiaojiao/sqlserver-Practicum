# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"我的报修", pos = wx.DefaultPosition, size = wx.Size( 606,363 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"\n我的报修\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer3.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.myfaultgrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.myfaultgrid.CreateGrid( 100, 6 )
		self.myfaultgrid.EnableEditing( True )
		self.myfaultgrid.EnableGridLines( True )
		self.myfaultgrid.EnableDragGridSize( False )
		self.myfaultgrid.SetMargins( 0, 0 )
		
		# Columns
		self.myfaultgrid.EnableDragColMove( False )
		self.myfaultgrid.EnableDragColSize( True )
		self.myfaultgrid.SetColLabelSize( 30 )
		self.myfaultgrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.myfaultgrid.SetColLabelValue(0,"设备编号") 
		self.myfaultgrid.SetColLabelValue(1,"申报人姓名") 
		self.myfaultgrid.SetColLabelValue(2,"申报日期") 
		self.myfaultgrid.SetColLabelValue(3,"所在实验室") 
		self.myfaultgrid.SetColLabelValue(4,"故障信息") 
		self.myfaultgrid.SetColLabelValue(5,"是否修复")
		
		# Rows
		self.myfaultgrid.EnableDragRowSize( True )
		self.myfaultgrid.SetRowLabelSize( 80 )
		self.myfaultgrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.myfaultgrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.myfaultgrid, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

