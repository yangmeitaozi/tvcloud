#!/usr/bin/env python
#coding:utf—8

import ConfigParser
import string
import os,sys
import MySQLdb
import xml_parse

def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))


class mysqldb:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("%s/set.ini" % (cur_file_dir()))
        self.db_host = config.get('db','host')
        self.db_port = string.atoi(config.get('db','port'))
        self.db_user = config.get('db','user')
        self.db_passwd = config.get('db','passwd')
        self.db_charset = config.get('db','charset')
        self.db_name = config.get('db','name')
        

def connect():
    db=mysqldb()
    conn =  MySQLdb.connect(host=db.db_host,user=db.db_user,passwd=db.db_passwd,\
                               db=db.db_name,port=db.db_port,charset=db.db_charset)
    return conn

class sqldb:
    def __init__(self,inifile):
        config = ConfigParser.ConfigParser()
        fn = "%s/"+inifile
        config.read(fn % (cur_file_dir()))
        self.db_host = config.get('db','host')
        self.db_port = string.atoi(config.get('db','port'))
        self.db_user = config.get('db','user')
        self.db_passwd = config.get('db','passwd')
        self.db_charset = config.get('db','charset')
        self.db_name = config.get('db','name')
        
def connects(inifile):
    db=sqldb(inifile)
    conn =  MySQLdb.connect(host=db.db_host,user=db.db_user,passwd=db.db_passwd,\
                               db=db.db_name,port=db.db_port,charset=db.db_charset)
    return conn

    
if __name__ == '__main__':
    conn=connect()
    cur = conn.cursor()
    cur.execute("""select id from order_list""")
    print(cur.fetchall())
    
