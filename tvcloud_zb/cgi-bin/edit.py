#!/usr/bin/env python
#coding=utf-8

import yate
import cgi
import mysql
import time
import cgitb
cgitb.enable()
from string import Template

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def tups(f):
    for each_tup in f:yield each_tup
        
form_data = cgi.FieldStorage()
print(yate.start_response())

dele_info = ''
subinfo=''

#Data from edit.py
try:       
    chid = form_data['chid'].value      
    sip = form_data['serverip'].value    
    spath = form_data['storagepath'].value
    status = form_data['status'].value
    subinfo = form_data['submit'].value   
    first_delet = """delete live_movie from live_movie,live_catalog where live_catalog.catalogid=live_movie.catalogid and live_catalog.chid=%s""" % chid
    dels = """delete live_catalog from live_catalog,live_channel where live_catalog.chid=live_channel.chid and live_channel.chid=%s""" % chid
    dele_info = """delete from live_channel  where chid=%s""" % chid
    update_url = """update  live_url set status=1 where  chid=%s""" % chid
    
    
except:
    pass

cid=''
#logoid = ''
sortid = ''
urlid = ''
#print form_data
#Data from publish.py
try:
    #cid = form_data['cid'].value    
    if "mix" in form_data:
        mix = form_data['mix'].value
        cid = int(mix.split(' ').pop(0))
        urlid = int(mix.split(' ').pop(1))
        #print urlid
    #logoid = form_data['logo'].value
    if "sortid" in form_data:
        sortid = form_data['sortid'].value
except:
    pass

conn = mysql.connect()
cursor = conn.cursor()


createtime = time.strftime("%H:%M:%S",time.localtime())
date = time.strftime("%Y-%m-%d",time.localtime())

get_statusid = """select statusid from live_status where sname='%s'""" %  u"发布".encode('utf-8')
cursor.execute(get_statusid)
stuid = cursor.fetchall()
statusid=''
if stuid != ():
    statusid = stuid[0][0]
message = """insert into live_channel (chid,statusid,createtime,date,sort_id) values(%s,%s,'%s','%s',%s) """% (cid,statusid,createtime,date,sortid)
message0 = """insert into live_channel (chid,statusid,createtime,date,sort_id,live_urlid) values(%s,%s,'%s','%s',%s,%s) """% (cid,statusid,createtime,date,sortid,urlid)
info = """select chid from live_channel """

#upd_live_url = """update live_url set serverid=%s,chid=%s where live_urlid=%s""" % (serverid,cid,urlid)


#Update from publish.py   
cursor.execute(info)
cid_mysql = cursor.fetchall()

"""
# if channelid has in order_list,no action 
"""
sig = 0
for each in tups(cid_mysql):   
    if cid and (int(cid) == each[0]):
        sig=1         
        break   

if not sig and cid and  urlid != '':  
    #print message0
    cursor.execute(message0)
    conn.commit()
#    cursor.execute(upd_live_url)
#   conn.commit()    


"""if serverid != '' and nid != '':
    print 'not null'
    cursor.execute(upd_live_url)
    conn.commit()
"""
#data from edit.py,updating,deleting]

if dele_info and subinfo==u'删除'.encode('utf-8') :   
    #print('execuse delete action')   
    cursor.execute(first_delet)
    conn.commit()
    cursor.execute(dels)
    conn.commit()
    cursor.execute(dele_info)
    conn.commit()
    #print 'delt channel'    
    #print 'delt url',delt_url
    cursor.execute(update_url)
    conn.commit()     
    



if subinfo==u'修改'.encode('utf-8'):
    #print 'reset'       
    cursor.execute("""select serverid from live_server where live_ip='%s'""" % sip)
    sidresult = cursor.fetchall()
    mysid =''
    if sidresult != ():     
        mysid = sidresult[0][0]    
        
    else:   
        m1 = """insert into live_server (live_ip) values ('%s'); """ % (sip,)  
        #print m1
        cursor.execute(m1)    
        conn.commit()
        cursor.execute("""select serverid from live_server where live_ip='%s'""" % (sip,))
        conn.commit()        
        sidresult = cursor.fetchall()
        mysid = sidresult[0][0]
   
        
    cursor.execute("""update  live_url set live_path='%s',serverid=%s,status=0 where chid=%s""" % (spath,mysid,chid) )   
    conn.commit()    
    
conn.close()

#select form order_list and show in tables
dics = {}
info = """select live_channel.chid,tvs_channel.chname,live_server.live_ip,live_url.live_path,live_status.sname """
info1 = """from tvs_channel,live_channel,live_server,live_url,live_status where tvs_channel.chid=live_channel.chid and """
info2 = """live_status.statusid=live_channel.statusid and live_url.live_urlid=live_channel.live_urlid and live_url.serverid = live_server.serverid """
info3 = """and live_url.status=0 order by live_channel.chid """

message = info + info1 + info2+info3
#print message
#newms = """select live_channel.chid,tvs_channel.chname,live_status.sname,live_url.live_path from tvs_channel,live_channel,live_status,live_url """
#newms = newms + """where tvs_channel.chid=live_channel.chid and live_status.statusid=live_channel.statusid and """
#newms = newms + """live_channel.live_urlid is null and live_url.chid=live_channel.chid order by live_channel.chid """
#print newms
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute(message)
result = cursor.fetchall()

#cursor.execute(newms)
#nres = cursor.fetchall()
#print 'nres',nres
conn.close()    
#print dics
print(yate.do_table_head())

for array in result:
    #print array[0]
    print(yate.do_table(array[0],array[1].decode('utf-8'),array[2],array[3],array[4].encode('utf-8'))) 
#for array in nres:
    #print(yate.do_table(array[0],array[1].decode('utf-8'),' ',array[3],array[2].encode('utf-8')))
print(yate.do_table_end("edit.py",u'删除'.encode('utf-8'),u'修改'.encode('utf-8')))


