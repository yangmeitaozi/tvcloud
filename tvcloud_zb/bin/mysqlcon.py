#!/usr/bin/env python
#coding:utf—8
import MySQLdb
import xml_parse 
import os,sys



class visitdb:
    def __init__(self,host,user,passwd,db,port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = int(port)
        self.db = db
    def signIn(self,message):
        conn = MySQLdb.connect(host=self.host,user=self.user,\
                               passwd=self.passwd,db=self.db,port=self.port,charset='utf8')
        cursor = conn.cursor()
        #cursor.execute("SET NAMES utf8")
        #conn.commit()
        cursor.execute(message)
        dic = cursor.fetchall()
        conn.close()
        return dic

class updatedb(visitdb):
    def __init__(self,host,user,passwd,db,port):
        visitdb.__init__(self,host,user,passwd,db,port)
    def update(self,message):
        conn = MySQLdb.connect(host=self.host,user=self.user,\
                               passwd=self.passwd,db=self.db,port=self.port,charset='utf8')
        cursor = conn.cursor()
        cursor.execute(message)
        conn.commit()
        conn.close()        



        
if __name__ == "__main__":
    pass

    
