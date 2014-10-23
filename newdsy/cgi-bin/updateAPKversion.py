#! /usr/bin/env python
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

sql = """select vername,url,vercode,describ,appname from live_apk_version """
vername = ''
url = ''
vercode = ''
describtion = ''
appname = ''

conn= mysql.connect()
cur = conn.cursor()
cur.execute(sql)
results = cur.fetchall()
print (yate.start_response('application/json'))

for row in results:   
    vername = row[0]
    url = row[1]
    vercode = row[2]
    describtion = row[3]
    appname = row[4].encode('utf-8')
    
versioninfo = {'versionname':vername,\
               'versioncode':vercode,\
               'apkurl':url,\
               'describtion':describtion,\
               'appname':appname
               }


print (json.dumps(versioninfo))
