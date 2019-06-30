
import wx 

#import the newly created GUI file 
import haveFindPwd as hp
class HpFrame(hp.MyFrame3):
	def nothing():
		pass

def do(text):
	app = wx.App() 
	frame = HpFrame(None)
	frame.pwd.SetValue(text) 
	frame.Show() 
	#start the applications 
	app.MainLoop()
