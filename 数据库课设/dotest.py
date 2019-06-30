# -*- coding: utf-8 -*-
# @Author: yezhipeng
# @Date:   2019-05-25 12:02:34
# @Last Modified by:   yezhipeng
# @Last Modified time: 2019-05-25 12:03:05
import wx
# 导入my_win.py中内容
import test

# 创建mainWin类并传入my_win.MyFrame1
class mainWin(test.MyFrame1):

   # 实现Button控件的响应函数showMessage
   def showMessage(self, event):
       self.m_textCtrl1.Clear()
       self.m_textCtrl1.SetValue('hello world')

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()

    main_win = mainWin(None)
    main_win.Show()

    app.MainLoop()