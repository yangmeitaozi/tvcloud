#! /usr/bin/env python
#coding:utf-8

import mysql
import cgi
import cgitb
cgitb.enable()
import yate
import logging
import os

results = ''
apname = ''
pircurl = ''
loadurl = ''
types = 0
position = 0 

sql = """select apname,pircurl,loadurl,types,position from live_indexpage where position=%s""" % position
get_all = """select apname,pircurl,loadurl,types,position from live_indexpage """
update = ("""update live_indexpage set apname='%s',pircurl='%s',loadurl='%s',types=%s where position=%s"""
          % (apname,pircurl,loadurl,types,position))

def DIR_NAME():
    return (os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'log')).replace('\\','/'))
                        
def get_results(message):   
    try:
        conn = mysql.connector()
        cur = conn.cursor()
        cur.execute(message)
        results = cur.fetchall()
        conn.close()
    except:
        return None    
    if results != () and len(result[0])==5:
        results = results[0]      
        ruturn(each[0],each[1],each[2],each[3],each[4])
    else:
        return None

    
def update_mydb(message):
    try:
        conn = mysql.connector()
        cur = conn.cursor()
        cur.execute(message)
        cur.commit()
        conn.close()    
    except:
        print 'update live_indexpage failure'


print(yate.start_response())
dirname = DIR_NAME()
logging.basicConfi(format = FORMAT,filemode='a+',level=logging.INFO,\
                    filename=dirname+'/indexpage.log')
        
form_data = cgi.FieldStorage() 
if 'position' in form_data:
    position = form_data['position']
    results = get_results(sql)
    if results:
        for each in results:
            apname = each[0]
            pircurl= each[1]
            loadurl= each[2]
            types = each[3]
            position = each[4]    
    print(yate.do_table_head())
    print(yate.sub_table(apname,pircurl,loadurl,types))    
    print(yate.do_table_end('indexedit.py'))

if 'apname' in form_data and 'picurl'in form_data and 'loadurl' in form_data and types in form_data and position in form_data:
    apname = form_data['apname']
    pircurl= form_data['picurl']
    loadurl= form_data['loadurl']
    types = form_data['types']
    position = form_data['position'] 
    print(yate.do_table_head())
    print(yate.do_table(key, cn, si, sp, ss))
    print(yate.do_table_end(myapp))
    print('update success!!!')



    
    