#!/usr/bin/env python
#coding:utf-8
####################
#cgi for movie_list which you can get programs' list
####################
import yate
import cgitb
#cgitb.enable()
import mysql
import json
import time,datetime
import cgi
import os
import logging

def cur_file_dir():
    return os.path.abspath(os.path.dirname(__file__))

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
    

def get_programInfo_from_store(catalogid):
    conn = mysql.connect()
    cursor = conn.cursor()
    message = """ select chid,catalogid,programid,program_name,start_time,timelength from live_movie where catalogid=%s order by programid""" % catalogid
    cursor.execute(message)    
    response = cursor.fetchall()
    conn.close()
    return(response)

def get_catalogid_from_store(cid=0,date=0):
    conn = mysql.connect()
    cur = conn.cursor()
    #print cid,date
    if cid == 0:
        if len(date) != 1:           
            message = """select catalogid from live_catalog where date = '%s'""" % (date,)            
        else:
            message = """select catalogid from live_catalog """
    elif cid != 0:
        if len(date) != 1:
            message = """select catalogid from live_catalog where date = '%s' and chid = %s """ % (date,cid)

        else:
            message = """select catalogid from live_catalog where chid = %s """ % (cid,)
    try:
        cur.execute(message)
        result = cur.fetchall()
        conn.close()
    except:        
        return None        
    return(result)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format = FORMAT,filemode='a+',level=logging.INFO,\
                    filename=cur_file_dir()+'/get_programs_cgi.log')


print(yate.start_response('application/json'))
try:
    form_data = cgi.FormContent()
except:
    logging.error('request failure')
    pass

cid = form_data.get('chid')

date = form_data.get('date')

status = ''
ls = []
results = ''
info = ''
if date == None or cid == None:   
    allprograms = {'status':'failure','count':0,'programs':None}                    
    print (json.dumps(allprograms))
else:   
    if isinstance(int(cid[0]),int):       
        if int(cid[0]) == 0:
            if len(date[0]) == 1:              
                catalogids = get_catalogid_from_store(date=date[0])                
                for each_id in catalogids:                  
                    results = get_programInfo_from_store(each_id[0])
                    ls.append(results)           
            else:                
                catalogids = get_catalogid_from_store(date=date[0])
                for each_id in catalogids:                 
                    results = get_programInfo_from_store(each_id[0])
                    ls.append(results)
            print(json.dumps(ls))
            
              
        elif cid != 0:            
            if len(date[0]) == 0:                
                catalogid = get_catalogid_from_store(cid[0])
                oj = []
                for each in catalogid:
                    results = get_programInfo_from_store(each[0][0])
                    oj.append(results)
                print (json.dumps(results))          
            else:               
                catalogid = get_catalogid_from_store(cid[0],date[0])
                print 'catalogid', catalogid
                if catalogid ==():
                    (y,m,d) = date[0].split('-',2)
                    dt = datetime.datetime(int(y),int(m),int(d))
                    dt = str(dt).split(' ').pop(0)                   
                    if dt > time.strftime("%Y-%m-%d",time.localtime()):
                        info = '%s is out of time' % (date[0])                        
                    else:
                        info = 'programs deleted'
                        
                else:                    
                    try:
                        results = get_programInfo_from_store(catalogid[0][0])
                        
                    except:
                        logging.error('get programs failure')
                        pass
                
                ls = []
                plist = {}               
                if results != () and  results != '':
                    logging.info('get programs success')
                    for each in results:
                        plist['chid'] = each[0]
                        plist['catalogid'] = each[1]
                        plist['programid'] = each[2]
                        plist['programName'] = each[3]
                        plist['startTime'] = each[4]
                        plist['timeLength'] = each[5]
                        milisec = get_miliseconds(each[4],date[0])
                        plist['gwtime'] = milisec
                        ls.append(plist)
                        plist = {}
                    status = 'success'
                else:                    
                    (y,m,d) = date[0].split('-',2)
                    dt = datetime.datetime(int(y),int(m),int(d))
                    dt = str(dt).split(' ').pop(0)                   
                    if dt > time.strftime("%Y-%m-%d",time.localtime()):
                        info = '%s is out of time' % (date[0])
                        logging.error('out of time,get programs failure,chid=%s,date=%s' % (cid,date))
                    else:
                        info = 'programs did not have'
                        logging.error('programs did not have,get programs failure,chid=%s,date=%s' % (cid,date))
                    status = 'failure'                                   
                    
                allprograms = {'info':info,'get_status':status,'chid_count':len(results),'programs':ls}                    
                print (json.dumps(allprograms))               

               
