# -*- coding: utf-8 -*-
# @Author: yezhipeng
# @Date:   2019-05-25 17:26:03
# @Last Modified by:   yezhipeng
# @Last Modified time: 2019-05-25 17:30:39
import wx 

#import the newly created GUI file 
import findPwdErr as fpe
class FpeFrame(fpe.MyFrame4):
	def nothing():
		pass

def do():
	app = wx.App() 
	frame = FpeFrame(None)
	frame.Show() 
	#start the applications 
	app.MainLoop()