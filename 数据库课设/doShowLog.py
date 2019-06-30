# -*- coding: utf-8 -*-
# @Author: yezhipeng
# @Date:   2019-05-26 22:30:20
# @Last Modified by:   yezhipeng
# @Last Modified time: 2019-05-27 15:19:38
import wx 

#import the newly created GUI file 
import connectSql	
import doShowLog
import showLog as sl
class SlFrame(sl.MyFrame5):
	lablist = []
	index = 0
	syear = '2019'
	smonth = '01'
	sday = '01'
	eyear = '2019'
	emonth = '01'
	eday = '01'
	tablelist1 = []
	tablelist2 = []

	def labidChoice( self, event ):
		SlFrame.index = event.GetEventObject().GetSelection()
	
	def syearChoice( self, event ):
		i = event.GetEventObject().GetSelection()
		SlFrame.syear = str(i+2017)
	
	def smonthChoice( self, event ):
		i = event.GetEventObject().GetSelection()
		if i+1<10:
			SlFrame.smonth = '0'+str(i+1)
		else:
			SlFrame.smonth = str(i+1)
	
	def sdaychoise( self, event ):
		i = event.GetEventObject().GetSelection()
		if i+1<10:
			SlFrame.sday = '0'+str(i+1)
		else:
			SlFrame.sday = str(i+1)
	
	def eyearChoice( self, event ):
		i = event.GetEventObject().GetSelection()
		SlFrame.eyear = str(i+2017)
	
	def emonthChoice( self, event ):
		i = event.GetEventObject().GetSelection()
		if i+1<10:
			SlFrame.emonth = '0'+str(i+1)
		else:
			SlFrame.emonth = str(i+1)
	
	def edayChoice( self, event ):
		i = event.GetEventObject().GetSelection()
		if i+1<10:
			SlFrame.eday = '0'+str(i+1)
		else:
			SlFrame.eday = str(i+1)

	def select( self, event ):
		labid = SlFrame.lablist[SlFrame.index]
		sdate = SlFrame.syear+SlFrame.smonth+SlFrame.sday
		edate = SlFrame.eyear+SlFrame.emonth+SlFrame.eday
		SlFrame.tablelist1 = connectSql.selectFixView(labid,sdate,edate)
		SlFrame.tablelist2 = connectSql.selectUnFixView(labid,sdate,edate)
		# print(SlFrame.tablelist1,SlFrame.tablelist2)
		# 清空
		for i in range(0,100):
			for j in range(0,8):
				self.fixedLog.SetCellValue(i, j, '')
		for i in range(0,100):
			for j in range(0,5):
				self.faultLog.SetCellValue(i, j, '')

		len1 = len(SlFrame.tablelist1)
		for i in range(0,len1):
			len2 = len(SlFrame.tablelist1[i])
			for j in range(0,len2):
				self.fixedLog.SetCellValue(i, j, SlFrame.tablelist1[i][j])
		len1 = len(SlFrame.tablelist2)
		for i in range(0,len1):
			len2 = len(SlFrame.tablelist2[i])
			for j in range(0,len2):
				self.faultLog.SetCellValue(i, j, SlFrame.tablelist2[i][j])
		

def do():
	SlFrame.lablist = connectSql.selectLabList()
	app = wx.App() 
	frame = SlFrame(None,100,100,SlFrame.lablist)
	frame.Show() 
	#start the applications 
	app.MainLoop()