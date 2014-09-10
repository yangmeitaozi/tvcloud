#!/usr/bin/env python
#coding:utf-8

import time
import mysql
import tvslist_updating
import catalog
import datetime 
import os
import logging

def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'log'))

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
dirname = cur_file_dir()
dirname = dirname.replace('\\','/')
logging.basicConfig(format = FORMAT,filemode='a+',level=logging.INFO,\
                    filename=dirname+'/update_catalog.log')

def find_n_time(dt):
    delta = datetime.timedelta(days=1)
    #print (dt)
    if isinstance(dt,datetime.datetime):
        y=dt.year
        m=dt.month
        d=dt.day        
    else:
        (y,m,d) = dt.split('-',2)   
   
    dt = datetime.datetime(int(y),int(m),int(d))
    dt = dt+delta
    dt = str(dt)   
    (date,hh) = dt.split(' ')       
    return date

#refresh catalog the day before now
def update_by_date():
    date_l = []
    conn = mysql.connect()
    cur = conn.cursor()
    sql = """SELECT count(DISTINCT date),min(date) FROM `live_catalog`; """
    sqls = """select distinct(date) from live_catalog;"""
    cur.execute(sql)    
    results = cur.fetchall()
    cur.execute(sqls)
    resu = cur.fetchall()    
    conn.close()
    print resu
    num = len(resu)    
    count = int(results[0][0])    
    min_d = results[0][1].encode('utf-8')      
    ft = int(min_d.split('-',2).pop(2))
    for i in range(num):        
        date_l.append(resu[i][0].encode('utf-8'))   
    dt = min_d
    while True:
        next_d = find_n_time(dt)
        dt = next_d       
        if next_d > time.strftime("%Y-%m-%d",time.localtime()):
            print 'out ot time',next_d
            break
        if next_d in date_l:               
                continue
        else:            
            print 'do something',next_d            
            print '------------------update-------------------'
            print '------------------%s-------------------' % next_d
            print '-------------------------------------------'
            update_catalog(next_d)
        
   
    
def update_catalog(date=''):
    cid = ''
    if date=='':
        date = time.strftime("%Y-%m-%d",time.localtime())
    ms = """select chid from live_channel where statusid=0 """
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(ms)
    dic_cid = cursor.fetchall()
    cids = []
    #print(dic_cid)
    for each in dic_cid:
        message = """insert into live_catalog (chid,date,status) values (%s,'%s',%s) """ % (each[0],date,0)
        ma = """select date from live_catalog where status = 0 and chid=%s""" % each[0]
        ms = """select date from live_catalog where chid=%s and date='%s' """ % (each[0],date)
        cursor.execute(ma)
        gets = cursor.fetchall()
        print ms
        cursor.execute(ms)
        result = cursor.fetchall()
        print 'select date',result        
        sl = []
        if gets:            
            for each in gets:
                sl.append(each[0])
                    
            try:
                if sl.index(date):                   
                    break
            except ValueError:
                logging.info('execute insert,chid=%s' % each[0])
                cursor.execute(message)
                conn.commit()
        elif result:
            print 'continue'
            continue
        else:
            print 'execute insert'
            logging.info('execute insert,chid=%s' % each[0])
            cursor.execute(message)
            conn.commit()
    conn.close()
    return 

def first_update():
    now = time.strftime('%H:%m',time.localtime())
    (hour,mini) = now.split(':')
    if int(hour) == 0 and int(mini) == 10:
        update_catalog()
        logging.info('updata catalog first time')
        print 'now',time.strftime('%H:%M:%S',time.localtime()) 
    else:
        print 'now',time.strftime('%H:%M:%S',time.localtime())
        
        

def produce():
    
    #logging.info('start')
    first_update()
    obj = tvslist_updating.mysql_loging()
    obj.tvsou_update_log      
    catalog.update()
    update_catalog()
              
   
    
if __name__=='__main__':

    #update_catalog()
    produce()
    #get_update_date()
    #update_by_date()
       
