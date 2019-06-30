
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
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):
	
	def __init__( self, parent,line1,line2, lablist ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"维修日志", pos = wx.DefaultPosition, size = wx.Size( 1000,850 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 15, 72, 90, 90, False, "黑体" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"\n维修日志\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		self.m_staticText46.SetFont( wx.Font( 30, 72, 90, 92, False, "华文隶书" ) )
		self.m_staticText46.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText46.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer5.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText211121 = wx.StaticText( self, wx.ID_ANY, u"实验室编号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211121.Wrap( -1 )
		self.m_staticText211121.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer2.Add( self.m_staticText211121, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		# labidChoices = []
		self.labid = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lablist, 0 )
		self.labid.SetSelection( 0 )
		self.labid.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer2.Add( self.labid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 14, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"日期：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		syearChoices = [ u"2017", u"2018", u"2019", u"2020", u"2021", u"2022", u"2023", u"2024", u"2025", u"2026", u"2027", u"2028", u"2029", u"2030" ]
		self.syear = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), syearChoices, 0 )
		self.syear.SetSelection( 2 )
		self.syear.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer1.Add( self.syear, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		smonthChoices = [ u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12" ]
		self.smonth = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), smonthChoices, 0 )
		self.smonth.SetSelection( 0 )
		self.smonth.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer1.Add( self.smonth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sdayChoices = [ u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31" ]
		self.sday = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), sdayChoices, 0 )
		self.sday.SetSelection( 0 )
		self.sday.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer1.Add( self.sday, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2111 = wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )
		self.m_staticText2111.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText2111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText21111 = wx.StaticText( self, wx.ID_ANY, u"至", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21111.Wrap( -1 )
		self.m_staticText21111.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText21111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		eyearChoices = [ u"2017", u"2018", u"2019", u"2020", u"2021", u"2022", u"2023", u"2024", u"2025", u"2026", u"2027", u"2028", u"2029", u"2030" ]
		self.eyear = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), eyearChoices, 0 )
		self.eyear.SetSelection( 2 )
		self.eyear.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer1.Add( self.eyear, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText212 = wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		self.m_staticText212.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		emonthChoices = [ u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12" ]
		self.emonth = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), emonthChoices, 0 )
		self.emonth.SetSelection( 0 )
		self.emonth.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer1.Add( self.emonth, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2112 = wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2112.Wrap( -1 )
		self.m_staticText2112.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText2112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		edayChoices = [ u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31" ]
		self.eday = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), edayChoices, 0 )
		self.eday.SetSelection( 0 )
		self.eday.SetFont( wx.Font( 11, 70, 90, 90, False, "黑体" ) )
		
		gSizer1.Add( self.eday, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText21112 = wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21112.Wrap( -1 )
		self.m_staticText21112.SetFont( wx.Font( 15, 72, 90, 90, False, "隶书" ) )
		
		gSizer1.Add( self.m_staticText21112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"已修复日志" ), wx.VERTICAL )
		
		self.fixedLog = wx.grid.Grid( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.fixedLog.CreateGrid( line1, 8 )
		self.fixedLog.EnableEditing( True )
		self.fixedLog.EnableGridLines( True )
		self.fixedLog.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.fixedLog.EnableDragGridSize( False )
		self.fixedLog.SetMargins( 0, 0 )
		
		# Columns
		self.fixedLog.EnableDragColMove( False )
		self.fixedLog.EnableDragColSize( True )
		self.fixedLog.SetColLabelSize( 30 )
		self.fixedLog.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.fixedLog.SetColLabelValue(0,"设备编号") 
		self.fixedLog.SetColLabelValue(1,"申报人姓名") 
		self.fixedLog.SetColLabelValue(2,"申报日期") 
		self.fixedLog.SetColLabelValue(3,"处理人姓名") 
		self.fixedLog.SetColLabelValue(4,"处理日期") 
		self.fixedLog.SetColLabelValue(5,"实验室编号") 
		self.fixedLog.SetColLabelValue(6,"设备损坏信息") 
		self.fixedLog.SetColLabelValue(7,"修复情况")
		
		# Rows
		self.fixedLog.EnableDragRowSize( True )
		self.fixedLog.SetRowLabelSize( 80 )
		self.fixedLog.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.fixedLog.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.fixedLog.SetFont( wx.Font( 15, 72, 90, 91, False, "华文隶书" ) )
		self.fixedLog.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.fixedLog.SetMaxSize( wx.Size( 1000,250 ) )
		
		sbSizer1.Add( self.fixedLog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"未修复日志" ), wx.VERTICAL )
		
		self.faultLog = wx.grid.Grid( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.faultLog.CreateGrid( line2, 5 )
		self.faultLog.EnableEditing( True )
		self.faultLog.EnableGridLines( True )
		self.faultLog.EnableDragGridSize( False )
		self.faultLog.SetMargins( 0, 0 )

		
		# Columns
		self.faultLog.EnableDragColMove( False )
		self.faultLog.EnableDragColSize( True )
		self.faultLog.SetColLabelSize( 30 )
		self.faultLog.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.faultLog.SetColLabelValue(0,"设备编号") 
		self.faultLog.SetColLabelValue(1,"申请人姓名")
		self.faultLog.SetColLabelValue(2,"申请时间")
		self.faultLog.SetColLabelValue(3,"实验室编号")
		self.faultLog.SetColLabelValue(4,"设备损坏信息")

		# Rows
		self.faultLog.EnableDragRowSize( True )
		self.faultLog.SetRowLabelSize( 80 )
		self.faultLog.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.faultLog.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.faultLog.SetFont( wx.Font( 15, 72, 90, 91, False, "黑体" ) )
		self.faultLog.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.faultLog.SetMaxSize( wx.Size( 800,250 ) )
		
		sbSizer11.Add( self.faultLog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		self.selectbtn = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.selectbtn.SetFont( wx.Font( 20, 72, 90, 92, False, "华文隶书" ) )
		
		bSizer5.Add( self.selectbtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.labid.Bind( wx.EVT_CHOICE, self.labidChoice )
		self.syear.Bind( wx.EVT_CHOICE, self.syearChoice )
		self.smonth.Bind( wx.EVT_CHOICE, self.smonthChoice )
		self.sday.Bind( wx.EVT_CHOICE, self.sdaychoise )
		self.eyear.Bind( wx.EVT_CHOICE, self.eyearChoice )
		self.emonth.Bind( wx.EVT_CHOICE, self.emonthChoice )
		self.eday.Bind( wx.EVT_CHOICE, self.edayChoice )
		self.selectbtn.Bind( wx.EVT_BUTTON, self.select )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def labidChoice( self, event ):
		event.Skip()
	
	def syearChoice( self, event ):
		event.Skip()
	
	def smonthChoice( self, event ):
		event.Skip()
	
	def sdaychoise( self, event ):
		event.Skip()
	
	def eyearChoice( self, event ):
		event.Skip()
	
	def emonthChoice( self, event ):
		event.Skip()
	
	def edayChoice( self, event ):
		event.Skip()
	
	def select( self, event ):
		event.Skip()
	