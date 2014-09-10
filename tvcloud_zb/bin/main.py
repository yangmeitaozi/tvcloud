import channellist_tvsoulist_updating
import update_catalog_list
import create_tables
import deal_update_movie
import update_movie_list
import time
import thread

create_tables()
channellist_tvsoulist_updating.update_channel_list()

def production():   
    while True:
        channellist_tvsoulist_updating.tvsou_update_log()        
        update_catalog_list()
        update_movie_list()
        time.sleep(600)

try:
    thread.start_new_thread(production,(,))
except:
    pass

