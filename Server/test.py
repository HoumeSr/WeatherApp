import psycopg2
import os

DATABASE = "postgresql://test_user:Stalker228@45.82.152.174:5432/test"
conn = psycopg2.connect(DATABASE, sslmode='require')
cur = conn.cursor()
#cur.execute("CREATE TABLE log(NUM INT);")
#cur.execute("INSERT INTO log(NUM) VALUES(12);")
cur.execute("SELECT * FROM log;")
#conn.commit()
s = cur.fetchall()
print(s)
cur.close()