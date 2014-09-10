#!/usr/bin/env python
#conding=utf-8

import pickle
import yate
import mysql
import cgitb
cgitb.enable()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#channel_list
allchannel = {}
allserver = {}
allstor_path = {}

conn = mysql.connect()
cur = conn.cursor()
cur.execute("""select chid,chname from tvs_channel where status=0""")
dic = cur.fetchall()
for each in dic:
    allchannel[each[0]]=each[1].encode('utf-8')
#print allchannel
#server ip and storage_addr  server_list

cur.execute("""select serverid,server_ip,storage_addr from live_server """)
ndic = cur.fetchall()
for eachs in ndic:
    allserver[eachs[0]] = eachs[1]    
    allstor_path[eachs[0]] = eachs[2]

#select logo url
cur.execute("""select logoid,chname from live_logo """)
logodic = cur.fetchall()
alllogoname = {}
for each in logodic:
    alllogoname[each[0]] = each[1].encode('utf-8')

#select catagory id
cur.execute("""select sort_id,sort_name from live_sort """)
catagorydic = cur.fetchall()
allcatagory = {}
for each in catagorydic:
    allcatagory[each[0]] = each[1].encode('utf-8')
    
print(yate.start_response())
print(yate.render_publish())
print(yate.start_form("edit.py"))    


print(yate.select('cid'))
print(yate.select_list_n(allchannel))
print(yate.end_select())

print(yate.select('catagory'))
print(yate.select_list_n(allcatagory))
print(yate.end_select())
"""
print(yate.select('serverip'))
print(yate.select_list_n(allserver))
print(yate.end_select())

print(yate.select('storagepath'))
print(yate.select_list_n(allstor_path))
print(yate.end_select())

print(yate.select('logo'))
print(yate.select_list_n(alllogoname))
print(yate.end_select())
"""
#print(yate.end_form("add"))
print(yate.submit())

