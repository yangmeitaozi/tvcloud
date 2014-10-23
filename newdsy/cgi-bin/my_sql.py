#!/usr/bin/env python
#coding:utf—8

import configparser
import string
import os,sys
import mysql.connector

def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))


class mysqldb:
    def __init__(self,filename):
        config = configparser.ConfigParser()
        config.read((cur_file_dir() + '/' + filename))
        self.db_host = config.get('db','host')
        self.db_port = config.getint('db','port')
        self.db_user = config.get('db','user')
        self.db_passwd = config.get('db','passwd')
        self.db_charset = config.get('db','charset')
        self.db_name = config.get('db','name')
        
        
def connect(fname='set.ini'):
    db = mysqldb(filename = fname)
    conn =  mysql.connector.connect(host=db.db_host,user=db.db_user,passwd=db.db_passwd,\
                               db=db.db_name,port=db.db_port,charset=db.db_charset)
    return conn

if __name__ == '__main__':
    print(cur_file_dir() + '/' + 'set.ini')
    conn = connect()
    cur = conn.cursor()
    cmdmsg = """select * from tvs_channel"""
    cur.execute(cmdmsg)
    print(cur.fetchall())
    
