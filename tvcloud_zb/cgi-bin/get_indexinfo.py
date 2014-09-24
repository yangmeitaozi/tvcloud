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

select1 = """SELECT u_apptype.type,u_items.appname,u_homepage.position,live_server.live_ip,live_url.live_path,u_items.logo 
FROM u_apptype,u_homepage,live_url,live_server,u_items WHERE live_server.serverid = live_url.serverid AND 
live_url.chid = u_items.chid and u_homepage.item_id= u_items.id AND u_items.type_id = u_apptype.id AND u_apptype.type = 1;"""

select2 = """SELECT u_apptype.type,u_items.appname,u_homepage.position,	u_items.dlurl,u_items.logo FROM	u_apptype,u_homepage,
u_items WHERE u_homepage.item_id = u_items.id AND u_items.type_id = u_apptype.id AND u_apptype.type = 0;"""

conn = mysql.connect()
cur = conn.cursor()
cur.execute(select1)
results = cur.fetchall()
cur.execute(select2)
results_n = cur.fetchall()


def return_json(result):   
    
    mylist = []
    mydic = {}
    status = ''
    info = ''
    if result == ():
        status = 'failure'
        info = 'get nothing'
    else:
        status = 'success'
        info = ''    
    
    for row in result:
        if row[0]==1:
            mydic['type']=row[0]
            mydic['name']=row[1].encode('utf-8')
            mydic['position']=row[2]
            mydic['loadurl']=row[3].encode('utf-8')+row[4].encode('utf-8')+'/now/live.m3u8'
            mydic['pircurl']=row[5].encode('utf-8')               
            mylist.append(mydic)
            mydic={}
        if row[0]==0:
            mydic['type']=row[0]
            mydic['name']=row[1].encode('utf-8')
            mydic['position']=row[2]
            mydic['loadurl']=row[3].encode('utf-8')
            mydic['pircurl']=row[4].encode('utf-8')                
            mylist.append(mydic)
            mydic={}
    myjson = {'status':status,'info':info,'message':mylist}
    return(json.dumps(myjson))
#print results+results_n   
print(return_json(results+results_n))
    
