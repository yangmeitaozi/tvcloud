#!/usr/src/env python
#coding:utf-8
import mysql
import urllib2
import xml.etree.ElementTree as Et

import cgitb
cgitb.enable()
import time,datetime
import os
import logging

def get_miliseconds(strtime,date):
    datestr = date+' ' + strtime
    #print 'time ',datestr
    tmlist = []
    array = datestr.split(' ')
    array1 = array[0].split('-')
    array2 = array[1].split(':')
    for v in array1:
        tmlist.append(int(v))
    for v in array2:
        tmlist.append(int(v))
    
    tmlist.append(0)
    tmlist.append(0)
    tmlist.append(0)
    tmlist.append(0) 
    if len(tmlist) != 9:
        return 0
    return int(time.mktime(tmlist))  

def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.curdir,os.path.pardir,'log'))


def get_chid(date):   
    message = """select chid,catalogid from live_catalog where date='%s' and (status=0 or status=2) order by chid """ % date    
   
    #select channelid for order_list
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    results = cursor.fetchall()
    print 'cids,',results
    conn.close()
    return (results)

def parse_xml(url,cataid):
    info = {}  
    pn = ''
    et = ''
    pdate = ''
    starttime = ''
    timelength=int()
    lists = []   
    try:
        furl = urllib2.urlopen(url)
    except urllib2.URLError as error:
        print 'URLError:',str(error)    
    
    f = furl.read()
    try:
        with open('programs.xml','w') as fp:
            for each_line in f:
                fp.write(each_line)
    except IOError as error:
        print('open file error:'+str(error))

    tree = Et.parse('programs.xml')
    root = tree.getroot()
    lst = root.getiterator('C')
    if len(lst)<2:
        mes = """update live_catalog set status=2 where date='%s' and catalogid=%s""" % (date,cataid)
        print(mes)
        cursor.execute(mes)
        conn.commit()
        return None
    for node in lst:        
        pt = node.find('pt').text
        #print(pt)
        pn = node.find('pn').text
        et = node.find('et').text
        pdate = pt.split(' ').pop(0)
        starttime = pt.split(' ')[1]
        (hour,min) = starttime.split(':')
        t = (int(hour))*60 + int(min)              
        tt = int()                
        if len(et)>8:
            et = et.split(' ')[1]       
            (hour,min,sec) = et.split(':',2)
            tt=(int(hour))*60 + int(min)            
            #print tt
            timelength = int(tt)+ (24*60-int(t))
        else:
            (hour,min) = et.split(':')
            tt=(int(hour))*60 + int(min)            
            #print tt
            timelength = int(tt)- int(t)                    
        lists.append([pn,pdate,starttime,timelength])
    return lists

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
dirname = cur_file_dir()
dirname = dirname.replace('\\','/')
logging.basicConfig(format = FORMAT,filemode='a+',level=logging.INFO,\
                    filename=dirname+'/update_movie.log')

def product():
    date = time.strftime("%Y-%m-%d",time.localtime())
    conn = mysql.connect()
    cursor = conn.cursor()
    results = get_chid(date)   
    
    url = 'http://hz.tvsou.com/jm/bjxest/data_ajJ9orFapp.asp'#?id=1&date=2014-06-30
    try:    
        for row in results:           
            urls = url+'?id=%s&date=%s'%(row[0],date)
            print 'get url',urls            
            logging.info('get url:%s' % urls)
            datas = parse_xml(urls,row[1])            
            if datas==None:
                logging.error('get data error,get None')
                continue
            logging.info('get data from tvsou OK')
            data_1 = tuple()
            data_2 = tuple()
            adata = []
            ndata = []
            for each_data in datas:                
                #adata.append((row[0],each_data[0],row[1],each_data[1],each_data[2],each_data[3]))
                #ndata.append((each_data[1],row[1])) 
                milisec = get_miliseconds(each_data[2], date)
                message = """insert into live_movie (chid,program_name,catalogid,date,start_time,timelength,gwtime) values(%s,'%s',%s,'%s','%s',%s,%s)""" % (row[0],each_data[0],row[1],each_data[1],each_data[2],each_data[3],milisec)
                conn = mysql.connect()
                cursor = conn.cursor()
                try:
                    cursor.execute(message)
                    conn.commit()                    
                except:
                    logging.error('update db failure')
                    print 'update db failure'
                ms = "update  live_catalog set status=1 where date='%s' and catalogid=%s" % (each_data[1],row[1])
                try:
                    cursor.execute(ms)
                    conn.commit()
                    conn.close()
                except:
                    logging.error('update live_catalog failure')
                    print 'db failure too'
                    pass
            logging.info('update db success')
    except:
        print'no action update movie'
        logging.info('no action update movie,chid=%s' % row[0])
        pass
                

if __name__ == '__main__':
    product()
    
    
    
    
        

        
