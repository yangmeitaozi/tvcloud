#!/usr/bin/env python
#_*_conding:utf-8_*_

import Osyate
from my_sql import connect   


def MacAdd():
    print(Osyate.start_response())
    print(Osyate.addOms())
    conn = connect('set_os.ini')
    cursor = conn.cursor()    
    cursor.execute("""select id,name from u_sp""")
    result = cursor.fetchall()
    conn.close()  
    print(Osyate.start_select_mac('deal_addMac.py'))
    for row in result:
        print(Osyate.sub_option({row[0]:row[1]}))
    print(Osyate.sub_pubend_next())    
    print(Osyate.include_footer())    
    
MacAdd()