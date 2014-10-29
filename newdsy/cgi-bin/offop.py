#!/usr/bin/env ptyhon
#coding:utf-8
from rice import editOsname
def offop():
    msg = ('''SELECT
    sp.name,sp.id,sta.status
    from u_sp as sp,
    u_hurl as url,u_status as sta where
    sp.id = url.spid 
    and url.statusid = 3 and url.statusid = sta.id''')    
    editOsname('项目下线','osOff.py',msg)
    
offop()