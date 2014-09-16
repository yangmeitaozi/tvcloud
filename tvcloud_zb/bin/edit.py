#!/usr/bin/env python
#coding=utf-8

import yate
import cgi
import mysql
import time
import cgitb
cgitb.enable()
from string import Template



def tups(f):
    for each_tup in f:yield each_tup
        
#update order_list 
form_data = cgi.FieldStorage()

print(yate.start_response())

#print 'form data,',form_data

dele_info = ''
try:    
    #deal the edit page    
    chid = form_data['chid'].value
    first_delet = """delete live_movie from live_movie,live_catalog where live_catalog.catalogid=live_movie.catalogid and live_catalog.chid=%s""" % chid
    dels = """delete live_catalog from live_catalog,live_channel where live_catalog.chid=live_channel.chid and live_channel.chid=%s""" % chid
    dele_info = """delete from live_channel  where chid=%s""" % chid
    #print(dele_info)

    sip = form_data['serverip'].value
    spath = form_data['storagepath'].value
    status = form_data['status'].value
    subinfo = form_data['submit'].value
    print 'subinfo,',subinfo
except:
    pass

cid=''
serverid=''
nid=''
#logoid = ''
catagoryid = ''
try:
    cid = form_data['cid'].value
    #serverid = form_data['serverip'].value
    #nid = form_data['storagepath'].value
    #logoid = form_data['logo'].value
    catagoryid = form_data['catagory'].value
except:
       pass
createtime = time.strftime("%H:%M:%S",time.localtime())
date = time.strftime("%Y-%m-%d",time.localtime())
message = """insert into live_channel (chid,statusid,createtime,date,sort_id) values(%s,%s,'%s','%s',%s) """% (cid,0,createtime,date,catagoryid)
info = """select chid from live_channel """

conn = mysql.connect()
cursor = conn.cursor()
if dele_info != '' and subinfo=='delete':
    #print('execuse delete action')
    cursor.execute(first_delet)
    conn.commit()
    cursor.execute(dels)
    conn.commit()
    cursor.execute(dele_info)
    conn.commit()
cursor.execute(info)
cid_mysql = cursor.fetchall()


"""if channelid has in order_list,no action """
sig = 0
for each in tups(cid_mysql):   
    if cid and (int(cid) == each[0]):
        sig=1         
        break   

if not sig and cid:  
    cursor.execute(message)
    conn.commit()
conn.close()


#select form order_list and show in tables
dics = {}
info = """select live_channel.chid,tvs_channel.chname,live_server.live_ip,live_server.storage_addr,live_status.sname """
info1 = """from tvs_channel,live_channel,live_server,live_status where tvs_channel.chid=live_channel.chid and """
info2 = """live_status.status=live_channel.statusid and live_server.chid=live_channel.chid order by tvs_channel.chid ASC """

message = info + info1 + info2
#print message

conn = mysql.connect()
cursor = conn.cursor()
cursor.execute(message)
result = cursor.fetchall()
conn.close()    
#print dics
print(yate.start_form('edit.py'))
print(yate.do_table_head())

for array in result:
    #print array[0]
    print(yate.do_table(array[0],array[1],array[2],array[3],array[4]))    
print(yate.do_table_end())


