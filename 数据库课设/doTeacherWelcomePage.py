
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 
import doMessageBox
import doEquipmentFix
import doEquipmentManagePage
import doSelectEquipment
import doSelectLab
import doShowLog
import TeacherWelcomePage as twp
class TwpFrame(twp.MyFrame2):
	def fixEquipment( self, event ):
		choiceChoices = connectSql.findEquipment()
		print(choiceChoices)
		doEquipmentFix.do(choiceChoices)

	
	def manageEquipment( self, event ):
		num = connectSql.countTotalFault() 
		labList = connectSql.selectLabList()
		doEquipmentManagePage.do(str(num),labList)
	
	def selectEquipment( self, event ):
		doSelectEquipment.do()
	
	def selectLab( self, event ):
		doSelectLab.do()
	
	def fixLog( self, event ):
		doShowLog.do()
	
	def teacherQuit( self, event ):
		self.Destroy()
	


def do():		
	app = wx.App() 
	frame = TwpFrame(None) 
	frame.Show() 
	#start the applications 
	app.MainLoop()
