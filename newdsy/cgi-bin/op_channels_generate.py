#!/usr/bin/env python
#coding=utf-8

import cgi
import printChannels 
import yate 
from original import *
from get_channels_cgi import json_channelsinfo

"""
product tv for server and stort tv list by sp_id
"""
def genetare_opchannels():
    obj = deal_mysql()
    results = get_formData('which_sp','which_channel')
    sp_id = results.pop(0)
    chidlist = results.pop(0)
    for element in chidlist:   
        msg = ('''insert into ulv_opchannels (sp_id,chid)
        select %s,%s from  DUAL WHERE  not exists 
        (SELECT sp_id,chid from ulv_opchannels WHERE sp_id=%s and chid=%s)'''
               % (sp_id, element, sp_id, element))
        
        obj.updateDb(msg)
    obj.Close()   
    '''
     #Store file to cache
    '''
    json_channelsinfo(int(sp_id))
    
    
    printChannels.print_operationboundary()

genetare_opchannels()