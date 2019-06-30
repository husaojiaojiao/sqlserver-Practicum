
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 

import doMessageBox
import doFixInfo
import equipmentFix as ef
class EfFrame(ef.MyFrame2):
	index = 0
	choiceChoices = []
	def makechoice( self, event ):
		EfFrame.index = event.GetEventObject().GetSelection()
	
	def fixIt( self, event ):
		_id = EfFrame.choiceChoices[EfFrame.index]
		info = connectSql.selectFixFaultView(_id)
		self.Destroy()
		doFixInfo.do(info)


def do(choiceChoices):
	EfFrame.choiceChoices = choiceChoices
	app = wx.App() 
	frame = EfFrame(None,choiceChoices) 
	frame.Show() 
	#start the applications 
	app.MainLoop()