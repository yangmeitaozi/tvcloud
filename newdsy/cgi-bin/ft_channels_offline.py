#!/usr/bin/env python
#coding=utf-8

import cgi
from printChannels import channels_offline
import yate 
from original import *

def ft_channels_off():
    #print(yate.start_response())
    obj = deal_mysql()
    form_data = cgi.FieldStorage()    
    chidlist = form_data.getvalue('which_channel') 
    '''
    #if  users checked one option the chidlist is a number,
    else if users checked more then one options, chidlist will be a list instance
    '''
    if isinstance(chidlist,list):
        for item in chidlist:
            msg1 = """delete from ulv_opchannels where chid=%s""" % int(item)
            #print(msg1)
            obj.updateDb(msg1)
            
            msg2 = """delete from ulv_genchannels where channel_id=%s""" % int(item)
            obj.updateDb(msg2)
            
            msg3 = """update tvs_channel set status=0 where chid=%s """ % int(item)
            obj.updateDb(msg3)
    else:
        msg1 = """delete from ulv_opchannels where chid=%s""" % int(chidlist)
        #print(msg1)
        obj.updateDb(msg1)
        
        msg2 = """delete from ulv_genchannels where channel_id=%s""" % int(chidlist)
        obj.updateDb(msg2)
        
        msg3 = """update tvs_channel set status=0 where chid=%s """ % int(chidlist)
        obj.updateDb(msg3)        
    obj.Close()
    channels_offline(True)

ft_channels_off()