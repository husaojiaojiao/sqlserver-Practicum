
import wx 

#import the newly created GUI file 
import connectSql	
import selectEquipment as se
class SeFrame(se.MyFrame3):
	def select( self, event ):
		equid = self.equid.GetValue()
		row = connectSql.selectEquipment(equid)
		labid = row[0]
		isfault = row[1]
		self.labid.SetValue(labid)
		if(isfault):
			self.statues.SetValue('不可使用')
		else:
			self.statues.SetValue('正常使用')
		

def do():
	app = wx.App() 
	frame = SeFrame(None)
	frame.Show() 
	#start the applications 
	app.MainLoop()