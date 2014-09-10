import mysql
import time
date = time.strftime("%Y-%m-%d",time.localtime())

cid_message = """select tvsou.channelid,tvsou.md5 from tvsou_update_list tvsou inner join order_list orl on orl.channelid=tvsou.channelid and date='%s' order by tvsou.channelid""" % date
cata_message = """select catalogid,channelid from catalog_list where date='%s'""" % date


conn = mysql.connect()
cursor = conn.cursor()
cursor.execute(cid_message)
tvsou_info = cursor.fetchall()
cursor.execute(cata_message)
cata_info = cursor.fetchall()
#print tvsou_info
#print cata_info
def flatten(nested):
    for each in nested:
        yield each
        
stup=[]        
for tup in flatten(tvsou_info):
    stup.append(tup)
#print stup   
sstup=stup
del_cid = []
for each in flatten(sstup):
    #if len(stup)>1:
    stup.remove(each)   
    for n in stup:      
        if each[1]==n[1]:            
            del_cid.append(each[0])
            break
print del_cid
del_catalogid = []
for n in del_cid:
    for each in flatten(cata_info):
        if n==each[1]:
            del_catalogid.append(each[0])
            break           
            

dele_message = []
for each in del_catalogid:
    dele_message.append(""" delete * from movie where catalogid=%s""" % each)

    
