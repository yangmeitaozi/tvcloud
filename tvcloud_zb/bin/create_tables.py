#!/usr/bin/env python
# -*- coding: cp936 -*-
#conding=utf-8
import mysql
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def create_tables():
    
    #-------------------------#
    """create table for tvsou"""
    #-------------------------#
    tvs_channel = """create table tvs_channel (chid int(11) not null auto_increment,tvid int(11),chname varchar(25),status int(11),primary key(chid))"""
    tvs_updatelog = """create table tvs_updatelog ( interface_id int(30) not null auto_increment primary key,chid int(11) not null ,p_date varchar(20),md5 varchar(255),create_datetime varchar(20))"""
    
    #-------------------------#
    """create tables for live"""
    #-------------------------#
    #live_sort
    live_sort = """ create table live_sort (sort_id int(11) not null auto_increment primary key,sort_name varchar(20))"""
    
    #live_channel
    live_channel = ("""create table live_channel (id int(11) not null auto_increment,chid int(11) not null unique,statusid int(11),
    live_urlid int(11),createtime varchar(11),date varchar(11),logoid int(11),sort_id int(11), primary key(id,chid))""")
    livechannel_fk_channelid = """alter table live_channel add  constraint tvs_channel_chid_fk foreign key(chid) references tvs_channel(chid)"""
    livechannel_fk_statusid = """alter table live_channel add constraint live_status_statusid_fk foreign key(statusid) references live_status (statusid)"""   
    livechannel_fk_logoid = """alter table live_channel add constraint live_logo_logoid_fk foreign key (logoid) references live_logo(logoid)"""
    livechannel_fk_sortid = """alter table live_channel add constraint live_catalog_classid_fk foreign key(sort_id) references live_sort (sort_id)"""
    livechannel_fk_live_urlid = """alter table live_channel add constraint live_url_urlid_fk foreign key (live_urlid) references live_url (live_urlid)"""
              
    
    live_url = """ create table live_url(live_urlid int(11) not null auto_increment primary key,chid int(11),serverid int(10),port int(10),live_path varchar(50),status int(11))"""
    
    live_logo = """ create table live_logo(logoid int(11) not null auto_increment primary key,chid int(11),serverid int(10),port varchar(10),path varchar(30),status int(10))"""
                 
    
    url_fk_sid = """alter table live_url add constraint live_logo_server_id_fk foreign key(serverid) references live_server(serverid)"""
    logo_fk_sid = """alter table live_logo add constraint live_logo_path_id_fk foreign key(serverid) references live_server(serverid)"""
    
    
    live_server = """create table live_server (serverid int(11) not null auto_increment primary key,live_ip varchar(25))"""
    live_status = """create table live_status (statusid int(11) not null auto_increment primary key,sname varchar(255))"""
    #live_catalog
    live_catalog = """create table live_catalog (catalogid int(11) not null auto_increment primary key,chid int(11),date varchar(20),status int(11))"""
    live_catalog_fk = """alter table live_catalog add constraint live_channel_chid_fk foreign key(chid) references live_channel(chid)"""
    #live_movie
    live_movie = """create table live_movie (programid int(11) not null auto_increment primary key,catalogid int(11),chid int(11),program_name varchar(255),date varchar(20),start_time varchar(20),timelength varchar(20),uri varchar(255),publish_status int(2))"""
    live_movie_fk = """alter table live_movie add constraint live_catalog_catalogid_fk foreign key(catalogid) references live_catalog (catalogid)"""


    
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute('drop table live_movie')
        conn.commit()
    except MySQLdb.OperationalError:
        pass
    
    try:
        cursor.execute('drop table live_catalog')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    try:
        cursor.execute('drop table live_channel')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    try:
        cursor.execute('drop table live_sort')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    try:
        cursor.execute('drop table live_catalog')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    try:
        cursor.execute('drop table tvs_channel')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    try:
        cursor.execute('drop table live_m3u8')
        conn.commit()
    except MySQLdb.OperationalError:
        pass
    
   
    try:
        cursor.execute('drop table live_url')
        conn.commit()
    except MySQLdb.OperationalError:
        pass  
    
    try:
        cursor.execute('drop table live_logo')
        conn.commit()
    except MySQLdb.OperationalError:
        pass 
            
    try:
        cursor.execute('drop table live_server')
        conn.commit()
    except MySQLdb.OperationalError:
        pass 


    try:
        cursor.execute('drop table live_status')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    try:
        cursor.execute('drop table tvs_updatelog')
        conn.commit()
    except MySQLdb.OperationalError:
        pass

    

    
    
    
    cursor.execute(tvs_channel)
    conn.commit()

    cursor.execute(tvs_updatelog)
    conn.commit()
   
    
 

    cursor.execute(live_sort)
    conn.commit()
    
    #sqli = """insert into live_sort values(%s,'%s')"""
    #cursor.execute("SET NAMES utf8")
    #conn.commit()
    #cursor.executemany(sqli,[(1,"央视"),(2,"卫视"),(3,"地方"),])
    #cursor.commit()
    
    cursor.execute(live_channel)
    conn.commit()

    cursor.execute(live_catalog)
    conn.commit()

    cursor.execute(live_movie)
    conn.commit()

    cursor.execute(live_url)
    conn.commit()
       

    cursor.execute(live_logo)
    conn.commit()
    
    cursor.execute(live_server)
    conn.commit()    
    
    cursor.execute(url_fk_sid)
    conn.commit()
    
    cursor.execute(logo_fk_sid)
    conn.commit()
    

    
    cursor.execute(live_status)
    conn.commit()
   

    
    cursor.execute(live_catalog_fk)
    conn.commit()

    cursor.execute(live_movie_fk)
    conn.commit()
    
    cursor.execute(livechannel_fk_channelid)
    conn.commit()
    
    cursor.execute(livechannel_fk_statusid)
    conn.commit()
    

    
    cursor.execute(livechannel_fk_logoid)
    conn.commit()

    cursor.execute(livechannel_fk_live_urlid)
    conn.commit()

    conn.close()


def update_list():
    
    conn = mysql.connect()
    cursor = conn.cursor()   
    cursor.execute("SET NAMES utf8")
    conn.commit()   
    cursor.execute("insert into live_server values(0,'http://zhibo.tv-cloud.cn')")
    sorts = [(1,u"央视".encode('utf-8')),(2,u"卫视".encode('utf-8')),(3,u"地方".encode('utf-8'))]
    status = [(0,u"发布".encode('utf-8')),(1,u"未发布".encode('utf-8')),(2,u"删除".encode('utf-8'))]
    for k in range(3):
        for i in range(3):
            sqli = """insert into live_sort values(%s,'%s')""" % sorts[i] 
            try:
                cursor.execute(sqli)
                conn.commit()    
            except:
                pass
        
        for n in range(3):
            sqln = """insert into live_status values(%s,'%s')""" % status[n]
            try:
                print sqln
                cursor.execute(sqln)
                conn.commit()
            except:
                pass        
    conn.close()
    
#if __name__=='__main__':
    #create_tables()