
import wx 

#import the newly created GUI file 
import connectSql	
import equipmentManagePage as emi
class EmiFrame(emi.MyFrame2):
	labList = []
	def OnChoice( self, event ):
		index = event.GetEventObject().GetSelection()
		labId = EmiFrame.labList[index]
		num = connectSql.countFault(labId)
		self.numOfTheLab.SetValue(str(num))

def do(num,labList):
	EmiFrame.labList = labList
	app = wx.App() 
	frame = EmiFrame(None,labList)
	frame.numOfFault.SetValue(num)
	frame.Show() 
	#start the applications 
	app.MainLoop()