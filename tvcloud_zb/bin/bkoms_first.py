#! /usr/bin/env python
#coding:utf-8
import mysql

from create_tables import create_tables,update_list
from tvslist_updating import mysql_loging

create_tables()
update_list()
myobj = mysql_loging()
myobj.update_channel_list

try:
    conn = mysql.connect()
    cursor = conn.cursor()   
    cursor.execute("SET NAMES utf8")
    conn.commit()   
    cursor.execute("insert into chmsdb.live_url (live_path,status) SELECT storage_addr,chid FROM tvcloud_zb.live_server;")
    conn.commit()
    conn.close()
except:
    pass