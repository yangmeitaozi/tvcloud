#!/usr/bin/env python
#conding=utf-8

import yate
import my_sql
import cgi
import time
import cgitb
cgitb.enable()
from string import Template
import sys

def channels():
    message = """select live_channel.chid,tvs_channel.chname,live_server.live_ip,live_url.live_path,live_status.sname """
    message += """from tvs_channel,live_channel,live_server,live_url,live_status where tvs_channel.chid=live_channel.chid and """
    message += """live_status.statusid=live_channel.statusid and live_url.live_urlid=live_channel.live_urlid and live_url.serverid = live_server.serverid """
    message += """and live_url.status=0 order by live_channel.chid """

    conn = my_sql.connect()
    cursor = conn.cursor()
    cursor.execute(message)
    result = cursor.fetchall()
    conn.close()
    
    headers = ["频道名称", "直播地址", "直播路径", "发布状态"]
    print(yate.start_response())
    print(yate.include_header("JSB living system"))
    print(yate.start_form("edit.py"))
    print(yate.start_table(tb_width="80%", tb_border="1px solid"))
    print(yate.tb_caption("已发布频道"))
    print(yate.tb_header(headers))

    for array in result:
        print(yate.tb_data(array[1:]))
    print(yate.end_table())
    print(yate.end_form())
    print(yate.include_footer({"Home": "/index.html"}))

channels()
