#!/usr/bin/env python
#conding=utf-8

import yate
import cgitb
#cgitb.enable()

the_links = [("频道上线", "channels_publish.py"),
             ("频道下线", "channels_offline.py"),
             ("频道维护", "channels_edit.py"),
             ("运营发布", "channels_operation.py"),
             ("新频道收录","channels_collect.py"),
             ("已发布频道", "channels_published.py"),
             ("首页内容更新","op_guidepage_infoadd.py"),
             ("首页内容发布","op_guidepage_set.py"),
            ]

print(yate.start_response())
print(yate.gen_left(the_links))
