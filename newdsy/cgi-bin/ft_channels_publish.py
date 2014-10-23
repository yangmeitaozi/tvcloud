#!/usr/bin/env python
#coding=utf-8

import yate
import cgi
import my_sql
import time
import cgitb
cgitb.enable()

import printChannels
from original import *

def channelop():
    respData = get_formData('channel_id','sort_id')
    obj = deal_mysql()
    msg=('''insert into ulv_genchannels (channel_id,sort_id) 
    select %s,%s from DUAL 
    WHERE  not exists (SELECT channel_id,sort_id from ulv_genchannels WHERE channel_id=%s and sort_id=%s)''' 
         % (respData[0],respData[1],respData[0],respData[1]))
    obj.updateDb(msg)
    msgn = """UPDATE tvs_channel set `status`=1 where chid=%s""" % respData[0]
    obj.updateDb(msgn)
    obj.Close()
    printChannels.channels_offline()    

channelop()