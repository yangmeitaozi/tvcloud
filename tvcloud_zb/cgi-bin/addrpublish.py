#! /usr/bin/env python 
#coding:utf-8

import yate
import mysql
import cgi
import cgitb
cgitb.enable()


print(yate.start_response())

#channel_list
allchannel = {}
allserver = {}
allstor_path = {}

conn = mysql.connect()
cur = conn.cursor()
cur.execute("""select chid,chname from tvs_channel where status=0 order by chid""")
dic = cur.fetchall()
for each in dic:
    allchannel[each[0]]=each[1].encode('utf-8')
#print allchannel
#server ip and storage_addr  server_list

cur.execute("""select live_server.serverid,live_server.live_ip from live_server """)
ndic = cur.fetchall()

for eachs in ndic:
    allserver[eachs[0]] = eachs[1] 

cur.execute("""select live_url.live_urlid,live_url.live_path,tvs_channel.chname from 
live_url,tvs_channel where live_url.chid = tvs_channel.chid and (live_url.status is null or live_url.status=1)""")
res = cur.fetchall()
conn.close()
for eachi in res:
    allstor_path[eachi[0]] = eachi[1]

 
#print(yate.start_response())
print(yate.render_addrpublish(urls="addrpublish.py"))
#print(yate.start_form("addrpublish.py"))    

print(yate.select_addr('cid'))
print(yate.select_list_new(allchannel))
print(yate.end_select())

print(yate.select('serverip'))
print(yate.select_list_n(allserver))
print(yate.end_select())

#print(yate.select('storagepath'))
#print(yate.select_list_new(allstor_path))
#print(yate.end_select())
print(' <td align="center" class="td_bg" width="25%" height="15" id="obj"><input type=text name="storagepath" id="txtHint"></td>')


"""
print(yate.select('logo'))
print(yate.select_list_n(alllogoname))
print(yate.end_select())
"""
#print(yate.end_form("add"))

print(yate.submit())

chid=''
serverid=''
urlid=''

#Data from publish.py

form_data = cgi.FieldStorage()
try:  
    #print form_data
    chid = form_data['cid'].value    
    if 'serverip' in form_data:
        serverid = form_data['serverip'].value
    if "storagepath" in form_data:
        urlid = form_data['storagepath'].value
    #logoid = form_data['logo'].value
    message = """update live_url set serverid=%s,status=0 where chid=%s and live_path=%s""" % (serverid,chid,urlid)
   
    #print message
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    conn.commit()
    conn.close()    
    
except:
    pass