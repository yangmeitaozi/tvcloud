#!/usr/bin/env python
#coding:utf-8
from my_sql import connect
import cgi
import Osyate

def off_spid():
    print(Osyate.start_response())
    form_data = cgi.FieldStorage(encoding='gbk')
    #print(form_data)
    spid = form_data.getvalue('osid',None)
    #print(spid)
    if spid != None:        
        conn = connect('set_os.ini')
        cursor = conn.cursor()
        msg = '''update u_hurl set statusid=2 where spid=%s''' % spid
        cursor.execute(msg)
        conn.commit()
        conn.close()  
        print('YOU HAVE DONE IT SUCCESS!')
        
off_spid()