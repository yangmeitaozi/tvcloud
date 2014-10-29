#!/usr/bin/env python
#coding:utf-8
from my_sql import connect
import cgi
import cgitb
from rice import editOsname

def deal_editOsname():
    osname = ''
    osid = ''
  
    '''
    Get data from cgi
    '''
    form_data = cgi.FieldStorage()
    #print form_data
    if 'osname' in form_data and 'osid' in form_data:
        osname = form_data['osname'].value
        osid = form_data['osid'].value
       
    
    conn = connect()
    cursor = conn.cursor()
    
    '''
    Update db if u_sp's data changed!
    '''
    if osname !='' and osid != '':
        ms = '''update u_sp set name="%s" where id=%s''' % (osname,osid)
        #print ms
        cursor.execute(ms)
        conn.commit()    
    editOsname()
        
deal_editOsname()