#!/usr/bin/env python
#conding=utf-8

import yate
import mysql
import cgi
import time
import cgitb
cgitb.enable()
from string import Template

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#select form order_list and show in tables
dics = {}
info = """select live_channel.chid,tvs_channel.chname,live_server.server_ip,live_server.storage_addr,live_status.sname """
info1 = """from tvs_channel,live_channel,live_server,live_status where tvs_channel.chid=live_channel.chid and """
info2 = """live_status.status=live_channel.statusid and live_server.chid=live_channel.chid order by live_channel.chid """

message = info + info1 + info2
#print message

conn = mysql.connect()
cursor = conn.cursor()
cursor.execute(message)
result = cursor.fetchall()
conn.close()    
#print dics
print(yate.start_response())
print(yate.render_temp_right())

for array in result:
    #print array[0]
    print(yate.do_normal_table(array[0],array[1],array[2],array[3],array[4])) 
print(yate.normal_table_end())

