
import wx 

## 数据库操作
import pymssql
import connectSql	

#import the newly created GUI file 

import doFindPwd
import doRegisteredPage
import doMessageBox
import doChangePwd
import LoginPage as lg
class LgFrame(lg.Login):
	# usrn = ''
	# 实现Button控件的响应函数Login
	def login( self, event ):
		username = self.inputUnm.GetValue()
		password = self.inputPwd.GetValue()
		if(username == ''):
			doMessageBox.do('请输入账号！')
		elif(password == ''):
			doMessageBox.do('请输入密码！')
		else:
			flag = connectSql.checkLogin(username,password)
			if(flag):
				# LgFrame.usrn = username 
				print('登陆成功')
			else:
				print('登陆失败')

	def register( self, event ):
		# 打开注册页
		doRegisteredPage.do()
		
	
	def forget( self, event ):
		# 跳出找回密码页面
		doFindPwd.do()
	def change( self, event ):
		# 修改密码
		doChangePwd.do()


if __name__ == '__main__':		
	app = wx.App() 
	frame = LgFrame(None) 
	frame.Show() 
	#start the applications 
	app.MainLoop()