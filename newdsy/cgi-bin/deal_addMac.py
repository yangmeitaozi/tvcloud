#!/usr/bin/env python
#_*_conding:utf-8_*_

import Osyate
import cgi
from my_sql import connect
from rice import editMac

def get_response():
    osname =''
    spid=''    
    pickosmac=''
    mac1=''
    mac2=''          
    #print(Osyate.start_response())           
    form_data = cgi.FieldStorage()     
    if form_data: 
        osname = form_data.getvalue('osname')
        spid = form_data.getvalue('spid')        
        pickosmac = form_data.getvalue('pickosmac')
        mac1 = form_data.getvalue('mac1')
        mac2 = form_data.getvalue('mac2')    
    
    conn = connect('set_os.ini')
    cursor = conn.cursor()
    if pickosmac is not None and pickosmac != '' and  ((mac1 is not  None and mac1 != '' ) or (mac2 is not None and mac2 != '')):       
        cursor.execute('''insert into u_devices (mac_l,mac_u,sp_id) values('%s','%s',%s)''' % (mac1,mac2,pickosmac))
        conn.commit()  
    editMac()

        
get_response()    