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
info = """select live_channel.chid,tvs_channel.chname,live_server.live_ip,live_url.live_path,live_status.sname """
info1 = """from tvs_channel,live_channel,live_server,live_url,live_status where tvs_channel.chid=live_channel.chid and """
info2 = """live_status.statusid=live_channel.statusid and live_url.live_urlid=live_channel.live_urlid and live_url.serverid = live_server.serverid """
info3 = """and live_url.status=0 order by live_channel.chid """

message = info + info1 + info2 + info3
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

