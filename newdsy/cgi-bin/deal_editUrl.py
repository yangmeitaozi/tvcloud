#!/usr/bin/env python
#_*_conding:utf-8_*_

from my_sql import connect
from rice import editUrl
import cgi


def deal_editUrl():
         conn = connect('set_os.ini')
         cur = conn.cursor()
         form_data = cgi.FieldStorage(encoding='gbk')
         mixid = form_data.getvalue('spid',None)
         ip = form_data.getvalue('ip',None)
         port = form_data.getvalue('port',None)
         submitValue = form_data.getvalue('submit',None)
         editinfo = '修改'
         deltinfo = '删除'
         
         if (mixid and ip and port and submitValue) is not None:                  
                  spid = int(mixid.split('&').pop(0))
                  hurlid = int(mixid.split('&').pop(1))
                  delMes = '''delete from u_hurl  where id=%s''' % hurlid
                  updMes = '''update u_hurl set ip='%s',port=%s where id=%s''' % (ip,port,hurlid)
                   
                  
                  if submitValue == editinfo:
                           cur.execute(updMes)
                           conn.commit()
                     
                  if submitValue == deltinfo:
                           cur.execute(delMes)
                           conn.commit()    
         editUrl()

deal_editUrl()