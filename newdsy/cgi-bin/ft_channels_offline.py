#!/usr/bin/env python
#coding=utf-8

import cgi
import printChannels 
import yate 
from original import *

def ft_channels_off():
    print(yate.start_response())
    obj = deal_mysql()
    form_data = cgi.FieldStorage()
    print(form_data.keys)
    chidlist = form_data.getvalue('which_channel')
    for item in chidlist:
        msg1 = """delete from ulv_opchannels where chid=%s""" % int(item)
        obj.updateDb(msg1)
        
        msg2 = """delete from ulv_genchannels where channel_id=%s""" % int(item)
        obj.updateDb(msg2)
        
        msg3 = """update tvs_channel set status=0 where chid=%s """ % int(item)
        obj.updateDb(msg3)
    obj.Close()
    printChannels.channels_offline(True)

ft_channels_off()