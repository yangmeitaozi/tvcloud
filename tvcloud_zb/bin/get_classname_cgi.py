#!/usr/bin/env python
#coding:utf-8

import yate
import cgi
import cgitb
cgitb.enable()
import mysql
import json


ms = ''

def get_classinfo_from_store(ms):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(ms)
    ca_data = cursor.fetchall()
    conn.close()
    return (ca_data)
    
print(yate.start_response('application/json'))

try:
    questing = cgi.FormContent()
    #print questing
except :
    pass
if 'quest' in questing.keys():
    quest_id = questing['quest']
    qid = quest_id[0]
    if qid == 0:
        ms = """select class_id,class_name from catagory_list"""
        print ms
    else:
        ms = """select class_id,class_name from catagory_list where class_id=%s""" % quest_id[0]
        print ms  
    ca_data = get_classinfo_from_store(ms)
    print ca_data
    
    
    print(json.dumps(ca_data))
      
