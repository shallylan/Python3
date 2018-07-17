# -*- coding: utf8 -*-

import pymysql
import pymysql.cursors
import json

#连接数据库
connect = pymysql.Connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = '',
	db = 'shiyanlou',
	charset = 'utf8'
	)

#打开游标
cursor = connect.cursor()

#打开文件且获取数据
def test1():
	with open('/Users/shallylan/Documents/用户:权限/data.json', 'rb') as file:
		test = json.loads(file.read())

	saveArr = []
	for i in test['data']['list']:
		#if iid 
		#	continue
		iid = test['data']['list'][i]['user']['iid']
		name = test['data']['list'][i]['user']['nickname']
		phone = test['data']['list'][i]['user']['phone']
		email = test['data']['list'][i]['user']['email']
		roleIds = test['data']['list'][i]['roleIds']
		roldNames = test['data']['list'][i]['roleNames']
		dateCreate = test['data']['list'][i]['user']['dateCreate']
		dateUpdate = test['data']['list'][i]['user']['dateUpdate']
				saveObj = [iid, name, phone, email, roleIds, roldNames, dateCreate, dateUpdate]
				saveArr.append(saveObj)

	#sql = "INSERT INTO statistics (`type`, `name`, `value`, `date`) VALUE (%s, %s, %s, %s) ";
	#cursor.execute(sql , saveArr[0])

	sql = "INSERT INTO job (`iid`, `name`, `phone`, `email`, `roldIds`, `roldNames`, `dateCreate`, `dateUpdate`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) ";
	#sql = "INSERT INTO statistics (`type`, `name`, `value`, `date`) VALUES(%s, %s, %s, %s) ";
	cursor.executemany(sql , (saveArr))

	connect.commit()
	connect.close()


test1()