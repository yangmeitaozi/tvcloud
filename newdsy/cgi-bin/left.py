#!/usr/bin/env python
#conding=utf-8

import yate
import cgitb
#cgitb.enable()

productList = [("频道上线", "channels_publish.py"),
             ("频道下线", "channels_offline.py"),
             ("频道维护", "channels_edit.py"),             
             ("新频道收录","channels_collect.py"),
             ("已发布频道", "channels_published.py")             
            ]

operationList = [("运营发布", "channels_operation.py"),
                 ("首页内容更新","op_guidepage_infoadd.py"),
                 ("首页内容发布","op_guidepage_set.py"),
                 ("运营项目增加",'addOsName.py'),
                 ("运营项目上线",'pubop.py'),
                 ("运营项目下线",'offop.py'),
                 ("EPG地址增加",'add_EpgUrl.py'),
                 ("EPG地维护",'editUrl.py'),
                 ("MAC地址增加",'add_mac.py'),
                 ("MAC地址维护",'deal_addMac.py')                 
                 ]


args1 = dict(listname='生产',elementId='id1',the_links=productList)
args2 = dict(listname='运营',elementId='id2',the_links=operationList)
print(yate.start_response())
print(yate.gen_left_ul(args1,args2))
