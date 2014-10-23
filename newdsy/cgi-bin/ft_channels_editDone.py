#!/usr/bin/env python
#coding=utf-8

import cgi
import printChannels 
import yate 
from original import *

def ft_channels_editDone():    
    obj = deal_mysql()
    result = get_formData('which_chid','which_addr')    
    msg1 = """UPDATE ulv_genaddress set gen_address='%s' where channel_id=%s""" % (result[1],result[0])
    obj.updateDb(msg1)        
    obj.Close()
    printChannels.ft_channels_editFirst()

ft_channels_editDone()