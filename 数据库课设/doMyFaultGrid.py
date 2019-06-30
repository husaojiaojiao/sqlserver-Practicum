
import wx 

#import the newly created GUI file 
import connectSql	
import doShowLog
import myFaultGrid as mg
class MgFrame(mg.MyFrame3):
	def nothing():
		pass

def do():
	app = wx.App() 
	frame = MgFrame(None)
	info = connectSql.myFaultView()
	length = len(info)
	print(info)
	for i in range(0,100):
		for j in range(0,6):
			frame.myfaultgrid.SetCellValue(i, j, '')
	for i in range(0,length):
		for j in range(0,5):
			frame.myfaultgrid.SetCellValue(i, j, info[i][j])
			if info[i][5]:
				frame.myfaultgrid.SetCellValue(i, 5, '已修复')
			else:
				frame.myfaultgrid.SetCellValue(i, 5, '未修复')
	frame.Show() 
	#start the applications 
	app.MainLoop()