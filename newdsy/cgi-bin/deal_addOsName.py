#!/usr/bin/env python
#_*_conding:utf-8_*_

import yate
import cgi
from my_sql import connect
from rice import EpgUrlAdd

def get_response():
    print(yate.start_response())
       
    form_data = cgi.FieldStorage(encoding='gbk')
    #print form_data
    
    osname =''
    spid=''
    
    
    if form_data:    
        osname = form_data.getvalue('osname')
        spid = form_data.getvalue('spid')       
    
    conn = connect('set_os.ini')
    cursor = conn.cursor()    
    if osname is not None and osname != '':     
        ms = """insert into u_sp (name) values('%s')""" % osname    
        cursor.execute(ms)
        conn.commit()
    EpgUrlAdd()

        
get_response()