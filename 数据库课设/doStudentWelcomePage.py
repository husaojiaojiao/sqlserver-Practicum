# -*- coding: utf-8 -*-
# @Author: yezhipeng
# @Date:   2019-05-25 21:11:58
# @Last Modified by:   yezhipeng
# @Last Modified time: 2019-05-27 19:22:40
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 
import doFindPwd
import doRegisteredPage
import doMessageBox
import doChangePwd
import doEquipmentRepair
import doMyFaultGrid
import myFaultGrid
import StudentWelcomePage as swp
class SwpFrame(swp.MyFrame3):
	def repair( self, event ):
		doEquipmentRepair.do()
	
	def myRepair( self, event ):
		doMyFaultGrid.do()


	
	def quit( self, event ):
		self.Destroy()
	
	


def do():		
	app = wx.App() 
	frame = SwpFrame(None) 
	frame.Show() 
	#start the applications 
	app.MainLoop()
