--创建设备维护数据库
create database EquipmentMaintenanceDatabase

--创建表 4
--equipment表\lab表\usr表\faultLog表
-----
--创建lab表
--字段 2
--实验室名称/id
--拥有计算机数量
create table lab
(
	lab_name char(3) not null primary key,
	cnt tinyint not null,
	check(cnt>0) 
)
-----
--创建equipment表
--字段 3
--设备id
--所在实验室名称
--是否故障
create table equipment 
(
	_id char(5) not null primary key,
	lab_name char(3) not null,
	isfault bit not null,
	foreign key(lab_name) references lab(lab_name)
)
--alter table equipment add isfault bit not null default(0)
-----
--创建usr表
--字段4
--姓名
--用户名
--密码
--是否是老师
create table usr
(
	username char(6) primary key not null,
	pwd char(6) not null,
	tea_name varchar(8) not null,
	isteacher bit not null,
)
--EXEC sp_rename 'usr.tea_name', 'name' , 'COLUMN'

-----
--创建faultLog表
--字段5
--自增id
--设备id
--故障信息
--申报时间
--是否修复
create table faultLog
(
	id int primary key IDENTITY(1,1) not null,
	equid char(5) foreign key references equipment(_id) not null,
	s_id char(6) foreign key references usr(username) not null,
	t_id char(6) foreign key references usr(username),
	sdate date not null,
	edate date,
	faultInfo varchar(1000) not null,
	isfix bit not null,
	check(edate>=sdate)
)
--drop table faultLog
--alter table faultlog add edate date not null
--插入数据
--lab表
insert into lab values('101',1)
insert into lab values('102',1)
insert into lab values('103',10)
insert into lab values('104',10)
insert into lab values('201',5)
insert into lab values('202',5)
insert into lab values('203',1)
insert into lab values('204',1)
--equipment表
insert into equipment values('10101','101',0)
insert into equipment values('10201','102',0)
insert into equipment values('10301','103',0)
insert into equipment values('10302','103',0)
insert into equipment values('10303','103',0)
insert into equipment values('10304','103',0)
insert into equipment values('10305','103',0)
insert into equipment values('10306','103',0)
insert into equipment values('10307','103',0)
insert into equipment values('10308','103',0)
insert into equipment values('10309','103',0)
insert into equipment values('10310','103',0)
insert into equipment values('10401','104',0)
insert into equipment values('10402','104',0)
insert into equipment values('10403','104',0)
insert into equipment values('10404','104',0)
insert into equipment values('10405','104',0)
insert into equipment values('10406','104',0)
insert into equipment values('10407','104',0)
insert into equipment values('10408','104',0)
insert into equipment values('10409','104',0)
insert into equipment values('10410','104',0)
insert into equipment values('20101','201',0)
insert into equipment values('20102','201',0)
insert into equipment values('20103','201',0)
insert into equipment values('20104','201',0)
insert into equipment values('20105','201',0)
insert into equipment values('20201','202',0)
insert into equipment values('20202','202',0)
insert into equipment values('20203','202',0)
insert into equipment values('20204','202',0)
insert into equipment values('20205','202',0)
insert into equipment values('20301','203',0)
insert into equipment values('20401','204',0)
--usr表
insert into usr values('010001','010001','老师1',1)
insert into usr values('010002','010002','老师2',1)
insert into usr values('010003','010003','老师3',1)
insert into usr values('020001','020001','学生1',0)
insert into usr values('020002','020002','学生2',0)
insert into usr values('020003','020003','学生3',0)
--faultLog表
insert into faultLog values('10101','020001',null,'20190526',Null,'显示器损坏',0)
insert into faultLog values('10201','020002',null,'20190524',Null,'CPU损坏',0)
insert into faultLog values('10301','020003','010003','20190522','20190522','主板损坏',1)
insert into faultLog values('10302','020001','010001','20190523','20190523','硬盘损坏',1)
insert into faultLog values('10303','020002','010001','20190523','20190524','硬盘损坏',1)
insert into faultLog values('10101','020001',NULL,'20190527',NULL,'显示器损坏',0)
-----
--创建视图
go
--fixFaultDetail视图
--包含设备编号、申报人姓名、申报日期、所在实验室、故障信息
create view fixFaultDetail(equId,sname,sdate,labId,faultInfo) with schemabinding
as
	select _id,tea_name,sdate,lab_name,faultInfo
		from dbo.faultLog join dbo.usr on faultLog.s_id = usr.username join dbo.equipment on faultLog.equid = equipment._id
go
drop view fixFaultDetail
go
--faultLog视图
--包含设备编号、申报人姓名、申报日期、修复人姓名、修复日期、所在实验室、故障信息
create view faultDetail(equId,sname,sdate,tname,edate,labId,faultInfo,fixIt)
as
	select _id,usr1.tea_name as sname,sdate,usr2.tea_name as tname,edate,lab_name,faultInfo,'已修复' as fixIt
		from faultLog join usr as usr1 on faultLog.s_id = usr1.username join equipment on faultLog.equid = equipment._id join usr as usr2 on faultLog.t_id = usr2.username
			where isfix = 1
go
go
--未修复视图日志
create view unfixFaultDetail(equId,sname,sdate,labId,faultInfo) with schemabinding
as
	select _id,tea_name,sdate,lab_name,faultInfo
		from dbo.faultLog join dbo.usr on faultLog.s_id = usr.username join dbo.equipment on faultLog.equid = equipment._id
			where isfix = 0
go
drop view unfixFaultDetail
--日志视图
go
create view faultLogView(equId,sname,s_id,sdate,labId,faultInfo,isfix) with schemabinding
as
	select _id,tea_name,s_id,sdate,lab_name,faultInfo,isfix
		from dbo.faultLog join dbo.usr on faultLog.s_id = usr.username join dbo.equipment on faultLog.equid = equipment._id
go
drop view faultLogView
--触发器
create trigger UpdateEquipment on faultLog after insert 
            for each row 
		   update equipment set isfault = 1 where _id = new.equid

CREATE TRIGGER UpdateEquipment
 ON faultLog
 
 for INSERT
 AS 
	declare @id char(5);
	select @id = equid from inserted
	update equipment set isfault = 1 where _id = @id
GO


--创建索引
CREATE UNIQUE CLUSTERED INDEX unFixFaultDetailIndex
ON unFixFaultDetail (equid DESC) 

--创建存储过程
go
Create proc sp_Insert_faultInfo
     @equid varchar(10),
     @username varchar(20),
     @sdate date,
     @info varchar(1000),
     @rtn int output
 as
     if ((select isfault from equipment where _id = @equid) = 1)
         begin
            set @rtn = 1
         end
     else
         begin
             insert into faultLog values(@equid, @username, NULL, @sdate, NULL,@info, 0)
             set @rtn=0
         end
drop proc sp_Insert_faultInfo
declare @rtn int
exec sp_Insert_faultInfo '20401','020001','2019-06-13','坏了',@rtn output
print @rtn

--测试
select pwd from usr where username  = '010001'
select count(pwd) from usr where username  = '01001'
update usr set pwd = '040404' where username = '020004'
select CONVERT (nvarchar(12),GETDATE(),112)
select _id from equipment where isfault = 1
select count(_id) from equipment where isfault = 1
select lab_name from lab
select * from fixFaultDetail where labId = '103' and sdate >='20190523' and sdate<='20190528' 
select * from fixFaultDetail where labId = '103' and sdate >='20190520' and sdate<='20190526'
select * from unfixFaultDetail where labId = '102' and sdate >='20190520' and sdate<='20190526'
select * from faultDetail where labId = '103' and sdate >='20190101' and sdate<='20190530'
select equid,sname,sdate,labId,faultInfo,isfix from faultLogView where s_id = '020001'