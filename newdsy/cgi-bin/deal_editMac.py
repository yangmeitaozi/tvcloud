#!/usr/bin/env python
#_*_conding:utf-8_*_
from rice import editMac
import Osyate
from my_sql import connect
import cgi

def deal_editMac():
    osname = ''
    osid = ''
    #print(Osyate.start_response())   
    form_data = cgi.FieldStorage(encoding='gbk')     
    conn = connect('set_os.ini')
    cur = conn.cursor()
 
    mid = form_data.getvalue('spid',None)
    mac1 = form_data.getvalue('mac1',None)
    mac2 = form_data.getvalue('mac2',None)
    submitinfo = form_data.getvalue('submit')
    deltinfo = '删除'
    updinfo = '修改'
    if (mid and mac1 and mac2) is not None:
        spid = int(mid.split('&').pop(0))
        devid = int(mid.split('&').pop(1))  
        deltMes = '''delete from u_devices where id=%s''' % devid
        updMes = '''update u_devices set mac_l='%s', mac_u= '%s' where id=%s''' % (mac1,mac2,devid)
     
        if submitinfo==deltinfo:
            print('deddd')
            cur.execute(deltMes)
            conn.commit()
        if submitinfo==updinfo:
            cur.execute(updMes)
            conn.commit()    
    editMac()
    
    
deal_editMac()