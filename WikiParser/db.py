import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost', user='root', password='', db='mysql',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
cur.execute('USE CollectIP')

def INSERT_DB(ip, country):
    cur.execute('SELECT * FROM ip_list WHERE ip = %s', (ip))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO ip_list (ip, country) VALUES(%s, %s)', (ip, country))
        cur.connection.commit()
