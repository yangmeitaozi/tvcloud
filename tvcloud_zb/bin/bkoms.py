import update_movie_list
import update_catalog_list
import time
while True:
    update_catalog_list.produce()
    update_movie_list.product()
    time.sleep(30)
    print '3 seconds sleep'
