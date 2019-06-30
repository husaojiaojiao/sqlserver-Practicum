# -*
# @Last Modified time: 2019-05-26 22:05:26
import wx 

#import the newly created GUI file 
import connectSql	
import selectLab as sb
class SbFrame(sb.MyFrame4):
	def select( self, event ):
		labid = self.labid.GetValue()
		cnt = connectSql.selectLab(labid)
		cntFault = connectSql.countFault(labid)
		self.totalNum.SetValue(str(cnt))
		self.faultNum.SetValue(str(cntFault))
		

def do():
	app = wx.App() 
	frame = SbFrame(None)
	frame.Show() 
	#start the applications 
	app.MainLoop()