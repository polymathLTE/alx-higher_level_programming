#!/usr/bin/python3
""" selects data from database that starts with N """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    st_list = cur.fetchall()
    for i in st_list:
        print(i)
    cur.close()
    db.close()
