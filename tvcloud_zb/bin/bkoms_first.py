#! /usr/bin/env python
#coding:utf-8
import mysql

from create_tables import create_tables,update_list
from tvslist_updating import mysql_loging

create_tables()
update_list()
myobj = mysql_loging()
myobj.update_channel_list

sqlobj = mysql.mysqldb()
dbname = sqlobj.db_name
print 'dabase name ',dbname
print '**************************'
try:
    conn = mysql.connect()
    cursor = conn.cursor()   
    cursor.execute("SET NAMES utf8")
    conn.commit()   
    dbnames = dbname + '.' + 'live_url'
    sqlmess = """insert into %s (chid,live_path) select sortnumber,bsstype from epgdb_live.publish_catalog where catalogcode='channel' """ % dbnames
    #print sqlmess
    cursor.execute(sqlmess)   
    conn.commit()
    conn.close()

except:
    pass