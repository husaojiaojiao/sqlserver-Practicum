

import wx 

#import the newly created GUI file 
import messageBox as mb
class MbFrame(mb.MyFrame6):
	def nothing():
		pass

def do(text):
	app = wx.App() 
	frame = MbFrame(None)
	frame.message.SetValue(text) 
	frame.Show() 
	#start the applications 
	app.MainLoop()

