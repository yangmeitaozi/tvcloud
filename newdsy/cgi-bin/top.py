#!/usr/bin/env python
#coding=utf-8
import yate
import cgitb

print(yate.start_response())
header = 'JSB 直播系统'


print(yate.render_temp_top(header))