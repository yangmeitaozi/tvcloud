#!/usr/bin/env python
#coding:utf-8
from my_sql import connect
import cgi
import cgitb
import Osyate


def editMac():
    conn = connect('set_os.ini')
    cur = conn.cursor()            
    '''
    #Print table on browser
    '''
    cur.execute('''select u_sp.id,u_devices.id,u_sp.name, u_devices.mac_l,u_devices.mac_u 
    from u_devices,u_sp,u_hurl 
    where u_sp.id=u_devices.sp_id and u_hurl.spid = u_sp.id and u_hurl.statusid <> 2 ''')
    results = cur.fetchall()
    conn.close()
    print(Osyate.start_response())
    print(Osyate.mac_t1())
    path = 'null'
    if results != ():
        for row in results:    
            mixid=''.join([str(row[0]),'&',str(row[1])])
            #print mixid
            print(Osyate.mac_t2(mixid,row[2],row[3],row[4]))
    print(Osyate.mac_t3('deal_editMac.py'))    
    print(Osyate.include_footer())
    
    
def editOsname(title,links,msg=None):    
        
    '''
    Substitute the template
    '''
    print(Osyate.start_response())
    conn = connect('set_os.ini')
    cursor = conn.cursor()
    if msg == None:
        msg= '''select name,id from u_sp'''    
    cursor.execute(msg)
    results = cursor.fetchall()
    conn.close()
    print(Osyate.osn_t1(title))
    
    if results != ():
        for row in results:
            print(Osyate.osn_t2(row[0],row[1],row[2]))
    print(Osyate.osn_t3(links))   
    print(Osyate.include_footer())   
    

def editUrl():

    print(Osyate.start_response())
    '''
    #Print table in browser
    '''
    conn = connect('set_os.ini')
    cur = conn.cursor()
    cur.execute('''select u_hurl.spid,u_hurl.id,u_sp.name,u_hurl.ip,u_hurl.port 
    from u_hurl,u_sp where u_sp.id=u_hurl.spid and u_hurl.statusid <> 2''')
    
    results = cur.fetchall()
    conn.close()
    title='地址管理'
    
    jsurl = '../js/edirUrl.js'
    print(Osyate.include_header(title,jsurl))
    print(Osyate.start_div(divId='editOsname', site='left'))
    print(Osyate.start_table(classname='table', width='100%', site='left'))
    print(Osyate.start_tr())
    tagname=['项目名称','地址','存储位置','端口号']
    for item in tagname:
        print(Osyate.table_th(classname='bg_tr', site='left', ms=item))
    print(Osyate.end_tr())
    path = 'null'
    if results != ():
        for row in results:   
            mixid = ''.join([str(row[0]),'&',str(row[1])])
            #print 'mixid',mixid
            print(Osyate.url_t2(mixid,row[2],row[3],path,row[4]))
    print(Osyate.end_table())
    print(Osyate.url_t3('deal_editUrl.py'))   
    print(Osyate.include_footer())
    
    
    
def EpgUrlAdd():
    print(Osyate.addOms())
    
    conn = connect('set_os.ini')
    cursor = conn.cursor()    
    cursor.execute("""SELECT
    sp.id,sp.name
    from u_sp as sp
    where 
    sp.id not in 
    (SELECT u_hurl.spid from u_hurl where u_hurl.statusid =2) 
    or sp.id not in (SELECT u_hurl.spid from u_hurl)""")
    result = cursor.fetchall()
    conn.close()
    print(Osyate.start_select_Epg('deal_addEpgUrl.py'))
    for row in result:    
        print(Osyate.sub_option({row[0]:row[1]}))        
    print(Osyate.sub_pubend())    
    print(Osyate.include_footer())  