#!/usr/bin/env python
#coding:utf-8

import mysql
import cgi
import cgitb
cgitb.enable()
import yate
import json
form_data = cgi.FieldStorage()
chid = ''
if "chid" in form_data:
    chid = form_data['chid'].value

print(yate.start_response('application/json'))
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("""select live_url.live_path from live_url,tvs_channel where tvs_channel.chid=live_url.chid and live_url.chid=%s""" % chid)
response = cursor.fetchall()
results = ''
if response != ():
    results = response[0][0]
    
print(json.dumps(results))