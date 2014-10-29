#!/usr/bin/env ptyhon
#coding:utf-8

from my_sql import connect
import Osyate
import cgi
import cgitb
cgitb.enable()




def pubop():  
        
    #title = u'预发布运营项目'.encode('utf-8')
    print(Osyate.addOms())
    print(Osyate.sub_form_addOsName('deal_addOsName.py'))  
    print(Osyate.include_footer())

pubop()