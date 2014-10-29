#/usr/bin/env python
#coding=utf-8

import yate
import cgi
import mysql
import cgitb
#cgitb.enable()
import json
from original import *
import os

def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

def Isdir(pathname):    
    if os.path.exists(pathname):
        return(True)
    else:
        return(False)

def Makedir(pathname):
    os.makedirs(cur_file_dir()+'/'+pathname)
 
def Checkdir(path):
    if Isdir(path):
        pass
    else:
        Makedir(path)
        
def getinfo(spid):  
  
    sql = """select apname,pircurl,loadurl,types,position from live_indexpage"""
    
    select1 = """SELECT
    u_apptype.type,
    u_items.appname,
    u_homepage.position,
    ulv_dns.dns_name,
    ulv_genaddress.gen_address,
    u_items.logo 
    FROM 
    u_apptype,
    u_homepage,
    ulv_dns,
    ulv_genaddress,
    u_items 
    WHERE
    ulv_dns.sp_id=%s
    AND 
    ulv_genaddress.channel_id = u_items.chid
    and u_homepage.item_id= u_items.id 
    AND u_items.type_id = u_apptype.id 
    AND u_apptype.type = 1 
    and ulv_dns.sp_id=u_homepage.spid
    order by u_homepage.position;""" % spid
    
    select2 = """SELECT 
    u_apptype.type,
    u_items.appname,
    u_homepage.position,
    u_items.dlurl,
    u_items.logo
    FROM
    u_apptype, 
    u_homepage,
    u_items,
    ulv_dns
    WHERE
    ulv_dns.sp_id=%s 
    and u_homepage.item_id = u_items.id
    AND u_items.type_id = u_apptype.id 
    AND u_apptype.type =0
    and ulv_dns.sp_id=u_homepage.spid
    order by u_homepage.position;""" % spid
    
    obj = deal_mysql()
    results = obj.askdata(select1)
    
    results_n = obj.askdata(select2)
    
    obj.Close()
    return(results+results_n)

def json_indexinfo(spid):   
    #print(yate.start_response("application/json"))    
    mylist = []
    mydic = {}
    status = ''
    info = ''
    result = getinfo(spid)
    if result == ():
        status = 'failure'
        info = 'get nothing'
    else:
        status = 'success'
        info = ''    
    
    for row in result:
        if row[0]==1:
            mydic['type']=row[0]
            mydic['name']=row[1]
            mydic['position']=row[2]
            mydic['loadurl']=row[3]+row[4]+'/now/live.m3u8'
            mydic['pircurl']=row[5]              
            mylist.append(mydic)
            mydic={}
        if row[0]==0:
            mydic['type']=row[0]
            mydic['name']=row[1]
            mydic['position']=row[2]
            mydic['loadurl']=row[3]
            mydic['pircurl']=row[4]              
            mylist.append(mydic)
            mydic={}
    myjson = {'status':status,'info':info,'message':mylist}
    #return(json.dumps(myjson))
    spdir = cur_file_dir() + '/spid_' + str(spid)
    Checkdir(spdir)
    with open(spdir+'/homepage.txt', mode='w+') as fd: 
        print(json.dumps(myjson),file=fd)    



    
    
