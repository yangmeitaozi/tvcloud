#!/usr/bin/env python
#coding:utf-8
####################
#cgi for order_list
####################
import yate
import cgi
import cgitb
cgitb.enable()
import mysql
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_channelInfo_from_store():
    m1 = """SELECT live_channel.chid,live_channel.sort_id,tvs_channel.chname,"""
    #m2 = """live_logo.ip,live_logo.path,live_url.live_ip,live_url.live_path from live_channel,tvs_channel,"""
    #m3 = """live_url,live_logo where live_channel.chid=tvs_channel.chid and live_channel.chid=live_logo.chid and live_channel.chid = live_url.chid order by live_channel.chid;"""  
    m2 = """live_server.live_ip,live_url.live_path from live_channel,tvs_channel,"""
    m3 = """live_url,live_server where live_channel.chid=tvs_channel.chid and """
    m4 = """live_channel.chid = live_url.chid and live_url.serverid=live_server.serverid and live_channel.live_urlid=live_url.live_urlid order by live_channel.chid;"""
    message = m1+m2+m3+m4
    print message
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    response = cursor.fetchall()
    conn.close()
    return(response)

    
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
   # print results  
   
    for each_cid in results:        
        datas["channelid"] = each_cid[0]        
        datas["channelname"] = each_cid[2]        
        datas['logoip'] = ''#each_cid[3]+each_cid[4]
        tail = each_cid[4]+'/now/live.m3u8'
        datas["live_uri"]= each_cid[3]+tail
        datas['sortid'] = each_cid[1]
        #if each_cid[1] == 1:            
        #    ys.append(datas)                      
            #print 'yangshi',ys
        #if each_cid[1]== 2:           
        #    ws.append(datas)                    
            #print 'weishi',ws
        #if each_cid[1]== 3:           
        #    df.append(datas)
            #print df
        alldata.append(datas)
        datas = {}
    #    datas = {}
    #yangshi['sort_list'] = ys
    #weishi['sort_list'] = ws
    #difang['sort_list'] = df
    #print ls
    #ls = [yangshi,weishi,difang]
    #print ls  
    all_channel_info['channellist']=alldata
            
    print(json.dumps(all_channel_info))
        
        
else:
    pass



