#!/usr/bin/env python
#coding:utf-8
####################
#cgi for order_list
####################
import yate
import os
import cgi
import cgitb
cgitb.enable()
import mysql
import json
import logging 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def cur_file_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_channelInfo_from_store():
    m1 = """SELECT live_channel.chid,live_channel.sort_id,tvs_channel.chname,"""
    m2 = """live_logo.ip,live_logo.path,live_server.server_ip,live_server.storage_addr from live_channel,tvs_channel,"""
    m3 = """live_server,live_logo where live_channel.chid=tvs_channel.chid and live_channel.chid=live_logo.chid and live_channel.chid = live_server.chid order by live_channel.chid;"""    
    message = m1+m2+m3
    #print message
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    response = cursor.fetchall()
    conn.close()
    return(response)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT,filemode='a+',level=logging.INFO,filename=cur_file_dir()+'/get_chanels_cgi.log')

    
print(yate.start_response('application/json'))

try:
    key_data = cgi.FormContent()
except:
    pass

ys = []
ws = []
df = []
datas = {}
alldata = []
all_channel_info = {}
yangshi = {'sort_id':1,'sort_name':'央视'}
weishi = {'sort_id':2,'sotr_name':'卫视'}
difang = {'sort_id':3,'sort_name':'地方'}

if key_data:   
    key_item = key_data['option']
    results = get_channelInfo_from_store()
    logging.info('get channels information from db success')
    for each_cid in results:       
        datas["channelid"] = each_cid[0]        
        datas["channelname"] = each_cid[2]        
        datas['logoip'] = each_cid[3]+each_cid[4]
        tail = each_cid[6]+'/now/live.m3u8'
        datas["live_uri"]= each_cid[5]+tail
        datas['sortid'] = each_cid[1]        
        alldata.append(datas)
        datas = {}    
    all_channel_info['channellist']=alldata
            
    print(json.dumps(all_channel_info))        
    logging.info('send json sucess')
else:
    logging.error('request failure')
    pass




