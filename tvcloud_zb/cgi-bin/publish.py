#!/usr/bin/env python
#conding=utf-8

import yate
import mysql
import cgitb
cgitb.enable()

#channel_list
allchannel = {}
allcatagory = {}

conn = mysql.connect()
cur = conn.cursor()

cur.execute("""select live_url.chid,live_url.live_urlid,tvs_channel.chname from tvs_channel,
live_url where tvs_channel.status=0 and live_url.status=0 and live_url.chid=tvs_channel.chid order by tvs_channel.chid""")
dic = cur.fetchall()
apd = ''
for each in dic:
    apd = ' '.join([str(each[0]),str(each[1])])
    allchannel[apd]=each[2].encode('utf-8')
    apd=''
#print allchannel

#select catagory id
cur.execute("""select sort_id,sort_name from live_sort """)
catagorydic = cur.fetchall()
conn.close()

for each in catagorydic:
    allcatagory[each[0]] = each[1].encode('utf-8')
    
print(yate.start_response())
print(yate.render_publish())
print(yate.start_form("edit.py"))    


print(yate.select('mix'))
print(yate.select_list_n(allchannel))
print(yate.end_select())

print(yate.select('sortid'))
print(yate.select_list_n(allcatagory))
print(yate.end_select())


"""
print(yate.select('logo'))
print(yate.select_list_n(alllogoname))
print(yate.end_select())
"""
#print(yate.end_form("add"))
print(yate.submit())

