#!/usr/bin/env python
#coding:utf—8
import MySQLdb
import xml_parse 
import os,sys
import ConfigParser
import string
import time


def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.curdir,os.path.pardir))

class mysql_loging():
    def __init__(self):        
        config = ConfigParser.ConfigParser()
        config.read("%s/set.ini" % (cur_file_dir()))
        self.db_host = config.get('db','host')
        self.db_port = string.atoi(config.get('db','port'))
        self.db_user = config.get('db','user')
        self.db_passwd = config.get('db','passwd')
        self.db_charset = config.get('db','charset')
        self.db_name = config.get('db','name') 
        
    @property        
    def update_channel_list(self):
        sqls = {}
        allchannel = xml_parse.parse_tvsou()
        print allchannel
        for key in allchannel.keys():
            cid = allchannel[key]['channelid']        
            cname = allchannel[key]['channelname']
            cname = MySQLdb.escape_string(cname.encode('utf-8'))        
            
            tvid = allchannel[key]['tvid']
            sql = """insert into tvs_channel (chid,tvid,chname,status) values(%s,%s,'%s',%s)""" % (cid,tvid,cname,0)
            print sql
            sqls[key]=sql
        conn = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,\
                               db=self.db_name,port=self.db_port,charset=self.db_charset)
        cursor = conn.cursor()
        cursor.execute("SET NAMES utf8")
        conn.commit()
        for key in sqls.keys():
            print(sqls[key])      
            cursor.execute(sqls[key])   
        conn.commit()
        conn.close()

    @property
    def tvsou_update_log(self):
        sqls = {}
        dic_channel = xml_parse.parse_tvsou_updatelog()
        datetime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        #print dic_channel
        if dic_channel == None:
            return None
        for key in dic_channel.keys():
            channelid = dic_channel[key]['ChannelID']
            pdate = dic_channel[key]['CatchDate']
            md5=dic_channel[key]['md5']
            interface_id=dic_channel[key]['interface_id']
            sql = """insert into  tvs_updatelog (chid,p_date,md5,interface_id,create_datetime) values(%s,'%s','%s',%s,'%s')""" \
              % (channelid,pdate,md5,interface_id,datetime)               
            sqls[key]=sql
        conn = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_passwd,\
                               db=self.db_name,port=self.db_port,charset=self.db_charset)
        cursor = conn.cursor()
        cursor.execute("SET NAMES utf8")
        conn.commit()
        sig = 0
        nosig = 0
        for key in sqls.keys():
            #print(sqls[key])
            try:
                cursor.execute(sqls[key])
                sig += 1
            except MySQLdb.IntegrityError as error:
                #print 'no update tvsou log'
                nosig += 1
                pass
        conn.commit()
        conn.close()
        print 'update count :',sig
        print 'no update count:',nosig
if __name__ == '__main__':
    obj = mysql_loging()
    #obj.tvsou_update_log
    obj.update_channel_list
    
    
