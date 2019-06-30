# -*
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 
import doMessageBox
import registeredPage as rg
class RgFrame(rg.MyFrame5):
	index = 0
	def OnChoice( self, event ):
		RgFrame.index = event.GetEventObject().GetSelection()
		print(RgFrame.index)
	def submit( self, event ):
		#提交注册信息
		username = self.username.GetValue()
		password1 = self.password1.GetValue()
		password2 = self.password2.GetValue()
		name = self.name.GetValue()
		choiceIndex = RgFrame.index
		if(username == ''):
			doMessageBox.do('账号不能为空！')
		elif(password1 == ''):
			doMessageBox.do('第一遍密码不能为空！')
		elif(password2 == ''):
			doMessageBox.do('第二遍密码不能为空！')
		elif(name == ''):
			doMessageBox.do('姓名不能为空！')
		elif(len(username) != 6):
			doMessageBox.do('账号必须为6位！')
		elif(len(password1) != 6):
			doMessageBox.do('密码必须为6位！')
		elif(len(name)>4):
			doMessageBox.do('姓名不能超过4个汉字！')
		else:
			mess = connectSql.registered(username,password1,password2,name,choiceIndex)
			self.Destroy()
			doMessageBox.do(mess)

		



def do():		
	app = wx.App() 
	frame = RgFrame(None) 
	frame.Show() 
	#start the applications 
	app.MainLoop()
