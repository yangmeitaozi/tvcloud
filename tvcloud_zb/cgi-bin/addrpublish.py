#! /usr/bin/env python 
#coding:utf-8

import yate
import mysql
import cgi
import cgitb
cgitb.enable()

form_data = cgi.FieldStorage()
chid=''
serverid=''
urlid=''

#Data from publish.py
try:
    chid = form_data['cid'].value    
    if 'serverip' in form_data:
        serverid = form_data['serverip'].value
    if "storagepath" in form_data:
        urlid = form_data['storagepath'].value
    #logoid = form_data['logo'].value
    message = """update live_url set chid=%s,serverid=%s,status=0 where live_urlid=%s""" % (chid,serverid,urlid)
    print message
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    conn.commit()
    conn.close()    
    
except:
    pass



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
cur.execute("""select live_urlid,live_path from live_url where status is null""")
res = cur.fetchall()
for eachi in res:
    allstor_path[eachi[0]] = eachi[1]

    
print(yate.start_response())
print(yate.render_addrpublish())
print(yate.start_form("addrpublish.py"))    


print(yate.select('cid'))
print(yate.select_list_n(allchannel))
print(yate.end_select())

print(yate.select('serverip'))
print(yate.select_list_new(allserver))
print(yate.end_select())

print(yate.select('storagepath'))
print(yate.select_list_new(allstor_path))
print(yate.end_select())
"""
print(yate.select('logo'))
print(yate.select_list_n(alllogoname))
print(yate.end_select())
"""
#print(yate.end_form("add"))
print(yate.submit())

    