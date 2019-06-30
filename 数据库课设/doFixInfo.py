
import wx 

#import the newly created GUI file 
import connectSql	
import fixInfo as fi
class FiFrame(fi.MyFrame3):
	_id = ''
	def makesure( self, event ):
		self.Destroy()
		connectSql.fixequipment(FiFrame._id)

def do(mess):
	FiFrame._id = mess[0]
	app = wx.App() 
	frame = FiFrame(None)
	frame.equid.SetValue(mess[0]) 
	frame.sname.SetValue(mess[1]) 
	frame.date.SetValue(mess[2]) 
	frame.labid.SetValue(mess[3]) 
	frame.info.SetValue(mess[4]) 
	frame.Show() 
	#start the applications 
	app.MainLoop()