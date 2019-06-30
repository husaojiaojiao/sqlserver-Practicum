
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 
import doMessageBox
import changePwd as cp
class CpFrame(cp.MyFrame2):
	def makesure( self, event ):
		#提交注册信息
		username = self.username.GetValue()
		password = self.password.GetValue()
		password1 = self.password1.GetValue()
		password2 = self.password2.GetValue()
		name = self.name.GetValue()
		print(password,password1,password2,len(password1))
		if(username == ''):
			doMessageBox.do('请输入账号！')
		elif(name == ''):
			doMessageBox.do('请输入姓名！')
		elif(password == ''):
			doMessageBox.do('请输入旧密码！')
		elif(password1 == ''):
			doMessageBox.do('第一遍密码不能为空！')
		elif(password2 == ''):
			doMessageBox.do('第二遍密码不能为空！')
		elif(password == password1):
			doMessageBox.do('新密码不能与旧密码一致！')
		elif(len(password1) != 6):
			doMessageBox.do('新密码必须为6位！')
		else:
			mess = connectSql.changePwd(username,name,password,password1,password2)
			self.Destroy()
			doMessageBox.do(mess)

		



def do():		
	app = wx.App() 
	frame = CpFrame(None) 
	frame.Show() 
	#start the applications 
	app.MainLoop()
