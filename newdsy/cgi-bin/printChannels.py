#!/usr/bin/env python
#coding=utf-8

import yate
import cgi
import my_sql
import time
import cgitb
#cgitb.enable()
import sys
from original import *

def channels_offline(channel_offline=True):
    message = ("""SELECT ulv_genchannels.channel_id,
    tvs_channel.chname, 
    ulv_genaddress.gen_address, 
    ulv_status.des
    FROM ulv_genchannels
    NATURAL JOIN tvs_channel, ulv_genaddress, ulv_status
    WHERE ulv_genchannels.channel_id = tvs_channel.chid 
    AND tvs_channel.chid = ulv_genaddress.channel_id 
    AND ulv_status.status_id=1 order by ulv_genchannels.sort_id, ulv_genchannels.channel_id""")

    conn = my_sql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    result = cursor.fetchall()
    conn.close()
    
    headers = ["频道名称", "频道编号", "直播路径", "发布状态"]
    print(yate.start_response())
    if channel_offline:
        print(yate.include_header("频道下线"))
    else:
        print(yate.include_header("已发布频道"))
    print(yate.start_form("ft_channels_offline.py"))
    print(yate.start_table(tb_width="100%", tb_border="1px solid"))
    print(yate.tb_header(headers))
    
    for array in result:
        print(yate.do_table(array, channel_offline))

    print(yate.end_table())
    if channel_offline==True:
        print(yate.end_form("确定"))
    
    
def channels_publish():
    cmdmsg = ("""SELECT tvs_channel.chid, tvs_channel.chname
    FROM tvs_channel
    NATURAL JOIN ulv_genaddress
    WHERE tvs_channel.`status` <> 1 AND tvs_channel.chid = ulv_genaddress.channel_id
    order by tvs_channel.chid""")
    
    conn = my_sql.connect()
    cur = conn.cursor()
    cur.execute(cmdmsg)
    result = cur.fetchall()
    
    msg = ("""select sort_id,sort_name from ulv_sort""")
    cur.execute(msg)
    sortinfo = cur.fetchall()
    conn.close()

    print(yate.start_response())
    print(yate.include_header("上线频道"))
    print("<p ><b>通过下面的复选框选择要上线的频道</b></p>")    
    print(yate.start_form("ft_channels_publish.py"))
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.start_row())
    print("<center>")   
    print(yate.select("channel_id"))
    print(yate.select_option(result))
    print(yate.end_select())  
    print('</center>')
    print(yate.end_row())
    
    print(yate.start_row())
    print("<center>")
    print(yate.select("sort_id"))
    print(yate.select_option(sortinfo))
    print(yate.end_select()) 
    print('</center>')
    print(yate.end_row())    
    
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())
    
def print_operationboundary():
    obj = deal_mysql('uspset.ini')
    msg = '''select id,name from u_sp;'''
    response = obj.askdata(msg)
    headers = ["运营商"]
    print(yate.start_response())
    print(yate.include_header("运营发布"))     
   
    print("<p ><b>点击下面的运营商名称可选择要发布的频道</b></p>")            
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.tb_header(headers))     
    print(yate.start_div('channel_div'))
    print(yate.start_form("op_channels_select.py"))
    for element in response:
        print('<tr><td>')        
        print(yate.radio_button("which_sp",element)) 
        print('</tr></td>')        
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())
    print(yate.end_div())          
    obj.Close()
    
def channels_operation(sp_id):  
    chidDic  = dict() #store the checked chid from sp_id
    obj = deal_mysql()
    
    msg = ('''SELECT ulv.channel_id,tvs.chname 
    from ulv_genchannels as ulv
    inner join tvs_channel as tvs
    on tvs.chid=ulv.channel_id order by ulv.sort_id, ulv.channel_id;''')
    
    msgn = ('''SELECT chid,sp_id from ulv_opchannels where sp_id=%d''' % int(sp_id))
    
    result = obj.askdata(msg)    
    checked = obj.askdata(msgn)
    for ele in checked:
        chidDic[ele[0]] = ele[1]
    nobj = deal_mysql('uspset.ini')
    msgs = '''select name from u_sp where id=%s''' % int(sp_id)
    response = nobj.askdata(msgs)
    
    headers = ["频道名称", "频道编号"]
    print(yate.start_response())
  
    print(yate.include_header("频道运营"))

    print(yate.start_form("op_channels_generate.py"))
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    theader = ['运营商']
    print(yate.tb_header(theader))
    print(yate.start_row())
    print('<input type="radio" checked="checked" name="which_sp" value="'+(sp_id)+'"/>"'+response[0][0]+'"')
    print(yate.end_row())
    print(yate.end_table())
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.tb_header(headers))
    for array in result:
        if chidDic.get(array[0],None)==None:
            print(yate.do_operationtable(array))
        else:
            print(yate.checked_operationtable(array))
    print(yate.end_table())
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())    
    obj.Close()
    nobj.Close()

def ft_channels_editFirst():    
    obj = deal_mysql()
    msg = ('''SELECT ulv.channel_id,tvs.chname 
    from ulv_genchannels as ulv
    inner join tvs_channel as tvs
    on tvs.chid=ulv.channel_id order by ulv.sort_id, ulv.channel_id;''')
    
    result = obj.askdata(msg)
    headers = ["频道名称"]
    print(yate.start_response())
    print(yate.include_header("频道维护"))       
    print(yate.start_form("ft_channels_edit.py"))
    print(yate.start_table(tb_width="100%", tb_border="1px solid"))
    print(yate.tb_header(headers))  
    print(yate.start_row())
    print(yate.select('which_chid'))
    #for array in result:        
    print(yate.select_option(result))
    print(yate.end_select())
    print(yate.end_row()) 
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())   
    obj.Close()
    

def ft_channels_edit_second():
    start_response()
    chid = get_formData('which_chid')
    obj = deal_mysql()
    msg = ("""SELECT ulv.channel_id,tvs.chname,ulv.gen_address 
    from ulv_genaddress as ulv inner join tvs_channel as tvs 
    on ulv.channel_id=tvs.chid and ulv.channel_id=%s""" % chid[0])
    result = obj.askdata(msg)
    info = result.pop(0)  
    headers = ["频道信息"]   
    print(yate.include_header("频道修改"))       
    print(yate.start_form("ft_channels_editDone.py"))
    print(yate.start_table(tb_width="100%", tb_border="1px solid"))
    print(yate.tb_header(headers))       
    print(yate.start_row())
    print(yate.checked_radio_button('which_chid',[info[0],info[1]]))
    print(yate.end_row()) 
    print(yate.start_row())
    print(yate.input_text("which_addr",info[2]))
    print(yate.end_row())     
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())
    obj.Close()  
    

def channels_collect():
    start_response()    
    obj = deal_mysql()
    msg = ("""SELECT chid,chname from tvs_channel where status=0""")         
    result = obj.askdata(msg)
    #info = result.pop(0)  
    headers = ["频道信息"]   
    print(yate.include_header("新频道收录"))       
    print(yate.start_form("ft_channels_collectDone.py"))
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.tb_header(headers))       
    print(yate.start_row())   
    print(yate.select('which_chid'))               
    print(yate.select_option(result))
    print(yate.end_select())    
    print('<input type="text" name="which_addr" />')
    print(yate.end_row())      
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())
    obj.Close()  
    
    
def channels_collect_submitdata():
    respData = get_formData('which_chid','which_addr')
    obj = deal_mysql()
    msg = ("""insert into ulv_genaddress (channel_id,gen_address) select %s,'%s' from DUAL 
    WHERE  not exists (SELECT channel_id,gen_address from ulv_genaddress WHERE channel_id=%s and gen_address='%s')"""
     % (respData[0],respData[1],respData[0],respData[1]))
    result = obj.updateDb(msg)
    obj.Close()        
    channels_collect()


def select_sp():    
    
    obj = deal_mysql("uspset.ini")
    msg =  '''select id,name from u_sp'''
    results = obj.askdata(msg)
    obj.Close()
    
    headers = ["运营商名称"]
    print(yate.start_response())
  
    print(yate.include_header("首页运营"))

    print(yate.start_form("op_guidepage_arrange.py"))    
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.tb_header(headers))
    for array in results:
        print(yate.start_row())
        print(yate.checked_radio_button('which_spid',[array[0],array[1]]))
        print(yate.end_row())
    print(yate.end_table())
    print(yate.start_table(tb_width="50%", tb_border="1px solid"))
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())
    print(yate.end_table())        
    
    
def guidpage_arrange():
    spid = get_formData('which_spid')
    obj = deal_mysql()
    msg = '''select id,alias from u_items'''
    results = obj.askdata(msg)
    
    nummsg = '''select item_id,position from u_homepage where spid=%s''' % spid[0]
    homeitem= obj.askdata(nummsg)   
    
    obj.Close()
    
    nobj = deal_mysql('uspset.ini')
    nmsg = """select name from u_sp where id=%s""" % spid[0]
    spname = nobj.askdata(nmsg)   
    nobj.Close()
      
    
    #headers = ["频道名称", "频道编号"]
    print(yate.start_response())
    aa = "频道运营"
    aa.encode('utf-8')
  
  
    print(yate.include_header(aa))

    print(yate.start_form("op_guidepage_storage.py"))
    
    print(yate.start_table(tb_width="75%", tb_border="1px solid"))    
    print(yate.start_row())
    print('<input type="radio" checked="checked" name="which_sp" value="'+(spid[0])+'"/>"'+spname[0][0]+'"')
    
    print(yate.end_row())
    print(yate.end_table())
    
    print(yate.start_table(tb_width="75%", tb_border="5px solid")) 
    '''
    spid has in u_homepage
    '''
    if homeitem !=():        
        position = dict()
        for eachItem in homeitem:
            position.update({eachItem[0]:eachItem[1]})
        for i in range(2):    
            print(yate.start_tr())
            for iters in range(3):
                if i == 1:
                    iters = iters + 3
                print(yate.start_td())
                pos = 'pos'+str(iters)
                print(yate.select(pos))
                for item in results:
                    if item[0] in position.keys() and position[item[0]]==iters+1:                        
                        print(yate.select_optione_with_selected(item,True))
                    else:
                        print(yate.select_optione_with_selected(item))                        
                print(yate.end_select())
                print(yate.end_td())
            print(yate.end_tr())
                     
    
    else:
        for i in range(2):                          
            print(yate.start_tr())        
            for iters in range(3):
                if i == 1:
                    iters = iters + 3
                print(yate.start_td())
                pos = 'pos'+str(iters)
                print(yate.select(pos))        
                print(yate.select_option(results))
                print(yate.end_select())
                print(yate.end_td())
            print(yate.end_tr())    
    
    print(yate.end_table())
    
    print(yate.start_table(tb_width="75%", tb_border="1px solid"))
    print(yate.start_row())
    print(yate.end_form("确定"))
    print(yate.end_row())    
    print(yate.end_table())  
    print('</body></html>')
    
if __name__ == '__main__':
    guidpage_arrange()