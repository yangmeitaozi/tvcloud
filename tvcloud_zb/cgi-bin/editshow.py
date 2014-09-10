#! /usr/bin/env python
#coding:utf-8

import mysql
import cgi
import cgitb
cgitb.enable()
import yate
import logging
import os

delete = """delete from live_indexpage where position=%s""" 

if 'delpos' in form_data:
    position = form_data['delpos']
    message = delete % position
    update_mydb(message)
                        
    results = get_results(get_all)

print(yate.start_response())
print('<a href=')