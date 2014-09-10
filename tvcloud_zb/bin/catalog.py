#!/usr/src/env python
#coding:utf-8

import mysql
import cgitb
cgitb.enable()
import time
#import update_movie_list

#yield 
def flatten(nested):
    for each in nested:
        yield each
        
#check time         
def format_time(time_string):
    tlen = len(time_string)
    if tlen < 3:
        original_format = '%s'       
    elif tlen < 6:
        original_format = '%Y-%m-%d'
        year = time.localtime().tm_year
        time_string = str(year)+'-'+time_string
    else:
        original_format = '%Y-%m-%d'
    time_string = time.strftime('%Y-%m-%d', time.strptime(time_string, original_format))
    return(time_string)

#return catalogid
def get_calogid(date):
    check_date = format_time(date)
    print 'check date',check_date
    conn = mysql.connect()
    cursor = conn.cursor()
    cid_message = """select tvsou.chid,tvsou.md5 from tvs_updatelog as tvsou,live_channel as orl where orl.chid=tvsou.chid and date='%s' order by tvsou.chid""" % check_date
    cata_message = """select catalogid,chid from live_catalog where date='%s'""" % check_date

    cursor.execute(cid_message)
    tvsou_info=cursor.fetchall()
    cursor.execute(cata_message)
    cata_info = cursor.fetchall()    
    stup=[]        
    for tup in flatten(tvsou_info):
        stup.append(tup)   
    sstup=stup[:]    
    del_cid = []
    for each in flatten(stup):
    #if len(stup)>1:
        sstup.remove(each)   
        for n in sstup:      
            if each[1]==n[1]:            
                del_cid.append(each[0])
                break    
    del_cid = list(set(del_cid))
    del_catalogid = []
    for n in del_cid:
        for each in flatten(cata_info):
            if n==each[1]:
                del_catalogid.append(each[0])
                break           
    conn.close()
    return (del_catalogid)

def update():
    now = time.strftime("%Y-%m-%d",time.localtime())
    deleting_catalogid = get_calogid(now)
    conn = mysql.connect()
    cursor = conn.cursor()
    if deleting_catalogid:
        print 'update catalogid set status=0'
        for each_id in deleting_catalogid:
            message = """update live_catalog set status=0 where catalogid=%s """ % (each_id)        
            cursor.execute(message)
            conn.commit()
            ms = """delete from live_movie where  catalogid=%s""" % each_id
            cursor.execute(ms)
            conn.commit()        
            
    conn.close()
    
if __name__ == '__main__':
   print (get_calogid('8-20'))
