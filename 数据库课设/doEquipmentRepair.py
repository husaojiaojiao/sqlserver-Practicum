
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 
import doMessageBox
import equipmentRepair as er
class ErFrame(er.MyFrame2):
	equipmentlist = []
	index = 0
	def onChoice( self, event ):
		ErFrame.index = event.GetEventObject().GetSelection()
	
	def makeSure( self, event ):
		faultinfo = self.faultInfo.GetValue()
		equid = ErFrame.equipmentlist[ErFrame.index]
		mess = connectSql.insertFaultLog(equid,faultinfo)
		self.Destroy()
		doMessageBox.do(mess)
		

def do():		
	equilist = connectSql.selectEquipmentId()
	ErFrame.equipmentlist = equilist
	app = wx.App() 
	frame = ErFrame(None,equilist) 
	frame.Show()
	#start the applications 
	app.MainLoop()