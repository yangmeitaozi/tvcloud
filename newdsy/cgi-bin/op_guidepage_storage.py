#!/usr/bin/env python
#coding=utf-8
from original import *
import cgi
from printChannels import select_sp
from get_indexinfo import json_indexinfo

def guidepage_storage():
    #print(yate.start_response())   
    getdata = get_formData('which_sp','pos0','pos1','pos2','pos3','pos4','pos5')    
    spid = getdata.pop(0)
    itemlist = getdata
    obj = deal_mysql()
    msgnn = '''delete from u_homepage where spid=%s''' % spid
    info = obj.updateDb(msgnn)
    i = 1   
    for element in itemlist:           
        msg = ('''insert INTO
        u_homepage(item_id,position,spid) 
        SELECT 
        %s,%s,%s 
        from DUAL 
        WHERE  not exists 
        (SELECT 
        item_id,
        position,
        spid 
        from 
        u_homepage 
        WHERE 
        item_id=%s and position=%s and spid=%s) ''' % (element,i,spid,element,i,spid))
        obj.updateDb(msg)        
        i += 1           
        
    obj.Close()
    json_indexinfo(int(spid))
    select_sp()
    
    
guidepage_storage()    