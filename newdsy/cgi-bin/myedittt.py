#!/usr/bin/env python
#coding=utf-8

import yate
import cgi
import my_sql
import time
import cgitb
cgitb.enable()
from string import Template
import sys
import json

def tups(f):
    for each_tup in f:yield each_tup
        
form_data = cgi.FieldStorage()

#print(yate.start_response('application/json'))
#print(json.dumps(form_data.getvalue('user')))
print(yate.start_response())
print(form_data.getvalue('user'))


'''print(json.dumps(form_data.getvalue('channel_id')))
print(json.dumps(form_data.getvalue('sort_id')))
print(json.dumps(form_data.getvalue('which_channel')))
print(json.dumps(form_data.getvalue('chid')))
print(json.dumps(form_data.getvalue('storagepath')))
#print(form_data['serverip'])
#print(form_data['storagepath'])
#print(form_data['status'])
#print(form_data['submit'])
'''