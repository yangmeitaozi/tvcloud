#!/usr/bin/env python
#coding:utf-8
####################
#cgi for catalog_list
####################
import yate
import cgitb
cgitb.enable()
import mysql
import json
import time
import cgi
import cPickle as pickle
import time,datetime

today = time.strftime('%Y-%m-%d',time.localtime())

def find_n_time(dt):
    delta = datetime.timedelta(days=1)
    #print (dt)
    if isinstance(dt,datetime.datetime):
        y=dt.year
        m=dt.month
        d=dt.day
        h=dt.hour
    else:
        (y,m,d) = dt.split('-',2)   
   
    dt = datetime.datetime(int(y),int(m),int(d))
    dt = dt-delta
    dt = str(dt)   
    (date,hh) = dt.split(' ')        
    return date

def get_catalogid_from_store(cid):
    message = """ select catalogid,date from catalog_list where channelid=%s""" % cid

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    dix = cursor.fetchall()
    conn.close()
    return dix

def get_pickle(cid):
    pass



print(yate.start_response('application/json'))
try:
    form_data = cgi.FormContent()
except:
    pass

if 'cid' in form_data.keys():
    cid = form_data['cid']  
    dix = get_catalogid_from_store(cid[0])        
    print(json.dumps(dix))

if __name__=='__main__':
    print find_n_time('2014-08-12')
    
    
