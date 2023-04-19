#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
    on cities.state_id=states.id where states.name = %s", (search, ))
    st_list = cur.fetchall()
    ls = list([i[0] for i in st_list])
    print(*ls, sep=', ')
    cur.close()
    db.close()
