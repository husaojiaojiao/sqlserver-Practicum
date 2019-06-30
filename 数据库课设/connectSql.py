
import pymssql
import datetime

import doMessageBox
import doTeacherWelcomePage
import doStudentWelcomePage
class gu:
	usrn = ''
class stu:
	usrn = ''
def conn():
    connect = pymssql.connect('DESKTOP-UILH2F2', 'sa', 'sa', 'EquipmentMaintenanceDatabase') #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    return connect

# print(conn())
# 验证登陆
def checkLogin(username,password):
	connect = conn()
	cursor = connect.cursor()
	sql = "select pwd,isteacher from usr where username = \'"+username+'\''
	cursor.execute(sql)
	row = cursor.fetchone()
	pwd = row[0]
	isteacher = row[1]
	cursor.close()   
	connect.close()
	if(pwd == password):
		if(isteacher):
			gu.usrn = username
			doTeacherWelcomePage.do()
		else:
			stu.usrn = username
			doStudentWelcomePage.do()
		return True
	else:
		doMessageBox.do('账号或密码错误！')
		return False
	

# print(checkLogin('010001','010001'))
# 找回密码
def findPwd(username,tea_name):
	connect = conn()
	cursor = connect.cursor()
	sql = "select tea_name,pwd from usr where username = \'"+username+'\''
	cursor.execute(sql)
	row = cursor.fetchone()
	# print(row[0],row[1])
	name = row[0]
	pwd = row[1]
	cursor.close()   
	connect.close()
	if(name == tea_name):
		return pwd
	else:
		return -1
# 注册
def registered(username,password1,password2,name,isteacher):
	connect = conn()
	cursor = connect.cursor()
	sql = "select count(pwd) from usr where username = \'"+username+'\''
	cursor.execute(sql)
	row = cursor.fetchone()
	cnt = row[0]
	if(cnt == 0):
		if(password1 == password2):
			sqlinsert = 'insert into usr values(%s,%s,%s,%d)'
			data = [(username,password1,name,isteacher)]
			cursor.executemany(sqlinsert,data)
			connect.commit()
			print('注册成功！')
			return '注册成功！'
		else:
			print('两次密码不一样！')
			return '两次密码不一样！'
	else:
		print('账号已存在！')
		return '账号已存在！'
# registered('010004','010004','010004','老师4',1)
# 修改密码
def changePwd(username,name,password,password1,password2):
	connect = conn()
	cursor = connect.cursor()
	sql = "select pwd,tea_name from usr where username = \'"+username+'\''
	sql1 = "select count(pwd) from usr where username = \'"+username+'\''
	cursor.execute(sql1)
	cnt = cursor.fetchone()
	if(cnt == 0):
		return '账号不存在！'
	else:
		cursor.execute(sql)
		row = cursor.fetchone()
		pwd = row[0]
		thename = row[1]
		if(pwd == password):
			if(thename == name):
				if(password1 == password2):
					sql2 = 'update usr set pwd = \''+password1+'\' where username = \''+ username+'\''
					cursor.execute(sql2)
					connect.commit()
					return '修改成功！'
				else:
					return '两次新密码不一样！'
			else:
				return '您输入的名字有误！'
		else:
			return '您输入的旧密码有误！'

# 查询待维修设备
def findEquipment():
	connect = conn()
	cursor = connect.cursor()
	sql = "select _id from equipment where isfault = 1"
	cursor.execute(sql)
	row = cursor.fetchone()
	choiceChoices = []
	while row:
		choiceChoices.append(row[0])
		# print(row[0])
		row = cursor.fetchone()
	cursor.close()   
	connect.close()
	return choiceChoices

# 修复待修复设备
def fixequipment(_id):
	connect = conn()
	cursor = connect.cursor()
	sql1 = "update equipment set isfault = 0 where _id = \'"+ _id+'\''
	cursor.execute(sql1)
	connect.commit()
	sql2 = "update faultLog set isfix = 1 where equid = \'"+ _id+'\''
	cursor.execute(sql2)
	connect.commit()
	sql3 = "update faultLog set t_id = \'"+ gu.usrn +"\' where equid = \'"+ _id+'\''
	cursor.execute(sql3)
	connect.commit()
	thedate = datetime.datetime.now().strftime('%Y%m%d')
	sql4 = "update faultLog set edate = \'"+ thedate +"\' where equid = \'"+ _id+'\''
	cursor.execute(sql4)
	connect.commit()
	doMessageBox.do('修复信息更新成功！')
	cursor.close()   
	connect.close()

# 损坏维修设备视图
def selectFixFaultView(_id):
	connect = conn()
	cursor = connect.cursor()
	sql = "select * from fixFaultDetail where equid = \'"+_id+'\''
	cursor.execute(sql)
	row = cursor.fetchone()
	info = []
	for i in [0,1,2,3,4]:
		info.append(row[i])
	cursor.close()   
	connect.close()
	return info

# 损坏总台数
def countTotalFault():
	connect = conn()
	cursor = connect.cursor()
	sql = "select count(_id) from equipment where isfault = 1"
	cursor.execute(sql)
	row = cursor.fetchone()
	num = row[0]
	cursor.close()   
	connect.close()
	return num

# 查询实验室列表
def selectLabList():
	connect = conn()
	cursor = connect.cursor()
	sql = "select lab_name from lab"
	cursor.execute(sql)
	row = cursor.fetchone()
	labList = []
	while row:
		labList.append(row[0])
		row = cursor.fetchone()
	cursor.close()   
	connect.close()
	return labList

# 查询实验室损坏台数
def countFault(labId):
	connect = conn()
	cursor = connect.cursor()
	sql = "select count(_id) from equipment where lab_name = \'" + labId + '\' and isfault = 1'
	cursor.execute(sql)
	row = cursor.fetchone()
	num = row[0]
	cursor.close()   
	connect.close()
	return num
	
# countFault('102')
# 设备查询
def selectEquipment(equid):
	connect = conn()
	cursor = connect.cursor()
	sql = "select lab_name,isfault from equipment where _id = \'" + equid + '\''
	cursor.execute(sql)
	row = cursor.fetchone()
	cursor.close()   
	connect.close()
	return row
# 实验室查询
def selectLab(labid):
	connect = conn()
	cursor = connect.cursor()
	sql = "select cnt from lab where lab_name = \'" + labid + '\''
	cursor.execute(sql)
	row = cursor.fetchone()
	cnt = row[0]
	cursor.close()   
	connect.close()
	return cnt
# 修复视图查询
def selectFixView(labid,sdate,edate):
	connect = conn()
	cursor = connect.cursor()
	sql = 'select * from faultDetail where labId = \'' + labid + '\' and sdate >=\'' + sdate + '\' and sdate<=\'' + edate + '\''
	print(sql)
	cursor.execute(sql)
	row = cursor.fetchone()
	tablelist = []
	rowlist = []
	while row:
		length = len(row)
		for i in range(0,length):
			rowlist.append(row[i])
		tablelist.append(rowlist)
		rowlist = []
		row = cursor.fetchone()
	return tablelist
# 未修复视图查询
def selectUnFixView(labid,sdate,edate):
	connect = conn()
	cursor = connect.cursor()
	sql = 'select * from unfixFaultDetail where labId = \'' + labid + '\' and sdate >=\'' + sdate + '\' and sdate<=\'' + edate + '\''
	print(sql)
	cursor.execute(sql)
	row = cursor.fetchone()
	tablelist = []
	rowlist = []
	while row:
		length = len(row)
		for i in range(0,length):
			rowlist.append(row[i])
		tablelist.append(rowlist)
		rowlist = []
		row = cursor.fetchone()
	return tablelist

# 设备编号查询
def selectEquipmentId():
	connect = conn()
	cursor = connect.cursor()
	sql = "select _id from equipment"
	cursor.execute(sql)
	row = cursor.fetchone()
	equipmentlist = []
	while row:
		equipmentlist.append(row[0])
		row = cursor.fetchone()
	cursor.close()   
	connect.close()
	# print(equipmentlist)
	return equipmentlist

# 报修并写入故障日志
def insertFaultLog(equid,faultInfo):
	username = stu.usrn
	username = '020001'
	sdate = datetime.datetime.now().strftime('%Y%m%d')
	isfix = 0
	connect = conn()
	cursor = connect.cursor()
	sql = 'declare @rtn int exec sp_Insert_faultInfo \''+ equid +'\',\''+ username +'\',\''+ sdate +'\',\''+ faultInfo +'\',@rtn output select @rtn'
	cursor.execute(sql)
	flag = cursor.fetchone()[0]
	print(flag)
	connect.commit()
	connect.commit()
	cursor.close()   
	connect.close()
	if flag==0:
		return '报修成功！'
	else:
		return '这台设备已经报修！'

# 我的报修查询
def myFaultView():
	connect = conn()
	cursor = connect.cursor()
	sql = "select equid,sname,sdate,labId,faultInfo,isfix from faultLogView where s_id = \'"+stu.usrn+'\''
	print(sql)
	cursor.execute(sql)
	row = cursor.fetchone()
	info = []
	while row:
		infolist = []
		for i in range(0,6):
			infolist.append(row[i])
		info.append(infolist)
		infolist = []
		row = cursor.fetchone()
	cursor.close()   
	connect.close()
	return info