#!/usr/bin/env python
#coding:utf-8

import yate
from original import * 

def info_add():
    start_response()
    #print(yate.start_response('text/plain;charset="UTF-8"'))
    obj = deal_mysql()
    msg = '''select id,comment from u_apptype '''
    items = obj.askdata(msg)
    msgs = '''SELECT ulv.channel_id,tvs.chname 
    from ulv_genchannels as ulv
    inner join tvs_channel as tvs
    on tvs.chid=ulv.channel_id; '''
    channel_items = obj.askdata(msgs)
    obj.Close()
    
    print(yate.render_guidepage_header('首页内容增加','首页内容增加','op_guidepage_infodeal.py','别名'))   
 
    
    print(yate.start_div('types'))
    print("<label for='types'>类型</label>")
    print(yate.start_select_onblur('types','types','setdisabled(this);'))
    print(yate.select_option(items))
    print(yate.end_select())
    print(yate.end_div())
    
    print(yate.render_guidepage_form('类型包名','logo地址'))
    
    print(yate.start_div('channel'))
    #print(yate.para('类型选择了APK请在URL栏输入地址，类型选择了频道请在频道下拉框中选一个相应的频道'))
    print("<label for='channel'>频道</label>")
    print(yate.select_id_name('channel','channel'))
    print(yate.select_option(channel_items))
    print(yate.end_select())
    print(yate.end_div())

    value = '确定' 
    print(yate.rend_guidepage_end(value))

    
    
info_add()