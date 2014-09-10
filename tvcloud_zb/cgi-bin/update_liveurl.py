#! /usr/bin/env python
#coding:utf-8
import mysql

def update_liveurl():
    
    sqlmess = """insert into chmsdb.live_url (chid,live_path) select sortnumber,bsstype from epgdb_live.publish_catalog where catalogcode='channel' """