#!/usr/bin/env python
#coding:utf-8
import my_sql
import yate
import cgi
import cgitb
#cgitb.enable()
from original import *
import json
import os

def get_channelInfo_from_store(spid):
    m1 = ("""SELECT ulv_opchannels.chid,
    tvs_channel.chname,
    ulv_dns.dns_name,
    ulv_genaddress.gen_address,    
    ulv_genchannels.sort_id
    from ulv_dns,ulv_genaddress,ulv_opchannels,ulv_genchannels,tvs_channel
    where ulv_opchannels.sp_id=%d 
    and ulv_dns.sp_id =%d 
    and ulv_genaddress.channel_id = ulv_opchannels.chid
    and tvs_channel.chid = ulv_opchannels.chid
    and ulv_genchannels.channel_id = ulv_opchannels.chid
    ORDER BY ulv_genchannels.sort_id, ulv_opchannels.chid""") % (spid,spid)
    
    conn = my_sql.connect()
    cursor = conn.cursor()
    cursor.execute(m1)
    response = cursor.fetchall()
    conn.close()
    return(response)

def cur_file_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

def Isdir(pathname):
    import os
    if os.path.exists(pathname):
        return(True)
    else:
        return(False)

def Makedir(pathname):
    os.makedirs(cur_file_dir()+'/'+pathname)
 
def Checkdir(path):
    if Isdir(path):
        pass
    else:
        Makedir(path)
        

def json_channelsinfo(spid):   
    
    datas = {}
    alldata = []
    all_channel_info = {}    
    
    results = get_channelInfo_from_store(spid)       
       
    for each_cid in results:        
        datas["channelid"] = each_cid[0]        
        datas["channelname"] = each_cid[1]        
        datas['logoip'] = ''
        tail = each_cid[3]+'/now/live.m3u8'
        datas["live_uri"]= each_cid[2]+tail
        datas['sortid'] = each_cid[4]
    
        alldata.append(datas)
        datas = {}      
    all_channel_info['channellist']=alldata
    spdir = cur_file_dir() + '/spid_' + str(spid)
    Checkdir(spdir)
    with open(spdir+'/channelslist.txt', mode='w+') as fd: 
        print(json.dumps(all_channel_info),file=fd)            
            
if __name__ == "__main__":
    json_channelsinfo(4)
    



