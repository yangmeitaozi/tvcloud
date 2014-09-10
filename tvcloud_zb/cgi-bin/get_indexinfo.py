#/usr/bin/env python
#coding=utf-8

import yate
import cgi
import mysql
import cgitb
cgitb.enable()
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

form_data = cgi.FieldStorage()

print(yate.start_response("application/json"))

sql = """select apname,pircurl,loadurl,types,position from live_indexpage"""
conn = mysql.connect()
cur = conn.cursor()
cur.execute(sql)
results = cur.fetchall()

mylist = []
mydic = {}
status = ''
info = ''
if results == ():
    status = 'failure'
    info = 'get nothing'
else:
    status = 'success'
    info = ''
    
for row in results:
    mydic['name']=row[0].encode('utf-8')
    mydic['pircurl']=row[1].encode('utf-8')
    mydic['loadurl']=row[2].encode('utf-8')
    mydic['type']=row[3]
    mydic['position']=row[4]
    mylist.append(mydic)
    mydic={}
myjson = {'status':status,'info':info,'message':mylist}
print(json.dumps(myjson))
    

    
