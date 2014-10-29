#!/usr/bin/env python
#_*_conding:utf-8_*_

import Osyate
import cgi
from rice import editUrl
from my_sql import connect

def get_response():    
    spid=''    
    ip=''
    port=''        
    #print(Osyate.start_response())           
    form_data = cgi.FieldStorage()     
    if form_data:        
        spid = form_data.getvalue('spid')        
        ip = form_data.getvalue('ip')
        port = form_data.getvalue('port')    
    
    conn = connect('set_os.ini')
    cursor = conn.cursor()
    if spid is not None and spid != '' and spid is not None and spid != '' and ip is not None and ip !='':
        cursor.execute('''insert into u_hurl (spid,ip,port,statusid) values(%s,'%s',%s,%s)''' % (spid,ip,port,1 ))
        conn.commit()
        conn.close()
    editUrl()

        
       

        
get_response()    