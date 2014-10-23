#!/usr/bin/env python
#coding:utf-8

import yate
from original import *
import json
import cgi
import cgitb
cgitb.enable()

def infodeal():
    start_response()
    form_data = cgi.FieldStorage(encoding='gbk')    
    
    channel = form_data.getvalue('channel',None)
    print('chid:',channel)
    url = form_data.getvalue('url',None)
    print('url:',url)
    alias = form_data.getvalue('alias',None)
    types = form_data.getvalue('types',None)
    appname = form_data.getvalue('appname',None)
    logo = form_data.getvalue('logo',None)
    #print('alias:',alias)
    print('types:',types)
    print('appname:',appname)
    print('logo:',logo)     
  
    #gdlist = get_formData('alias','types','appname','logo','channel','url')
    
    obj = deal_mysql()
    
    '''
    #Deal of channel
    '''
    if channel!=None and alias!=None and types!=None and appname!=None and logo!= None:
        msg = '''insert into u_items(alias,type_id,appname,logo,chid) values('%s',%s,'%s','%s',%s)''' % (alias,
                                                                                                         types,
                                                                                                         appname,
                                                                                                         logo,channel)
        obj.updateDb(msg)
        
   
    elif  url!=None and alias!=None and types!=None and appname!=None and logo!= None:  #Deal of apk
        msgs = '''insert into u_items(alias,type_id,appname,logo,dlurl) values('%s',%s,'%s','%s','%s')''' % (alias,types,appname,logo,url)
        obj.updateDb(msgs)        
        
    else:
        
        print(json.dumps('更新不成功，请返回重新输入数据'))
        return
    print('update data success!')              
    obj.Close()
    
  
    
infodeal()