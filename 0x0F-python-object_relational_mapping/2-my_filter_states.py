#!/usr/bin/python3

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]
search = sys.argv[4]

db = MySQLdb.connect(user=username, passwd=password, db=dbname)
cur = db.cursor()

cur.execute(f"select * from states where name = '{search}'")
st_list = cur.fetchall()
for i in st_list:
    print(i)
cur.close()
db.close()
