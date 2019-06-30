# -*- coding: utf-8 -*-
# @Author: yezhipeng
# @Date:   2019-05-25 16:43:19
# @Last Modified by:   yezhipeng
# @Last Modified time: 2019-05-25 19:31:25
import wx 
import pymssql
import connectSql
  
#import the newly created GUI file 
import findPwdPage as fp
import doHaveFindPwd
import doMessageBox
import doFindPwdErr
class FpFrame(fp.MyFrame2):
	# 实现Button控件的响应函数Login
	def findPwd( self, event ):
		##findPwd
		username = self.findInputUnm.GetValue()
		tea_name = self.findInputName.GetValue()
		if(username == ''):
			doMessageBox.do('请输入账号！')
		elif(tea_name == ''):
			doMessageBox.do('请输入老师姓名！')
		else:
			# print(username,tea_name)
			flag = connectSql.findPwd(username,tea_name)

			if(flag == -1):
				doFindPwdErr.do()
				print('您输入的账号或教师姓名有误！')
			else:
				doHaveFindPwd.do(flag)
				print('密码为',flag)

def do():
	app = wx.App() 
	frame = FpFrame(None) 
	frame.Show() 
	#start the applications 
	app.MainLoop()

