import mysql
sql = """insert into chmsdb.live_server (cname,server_ip,storage_addr) SELECT catalogname,left(hiscatalogpicurl1,24),bsstype FROM epgdb_live.`publish_catalog`;"""
conn = mysql.connect()
cur = conn.cursor()
cur.execute(sql)
results = cur.fetchall()



