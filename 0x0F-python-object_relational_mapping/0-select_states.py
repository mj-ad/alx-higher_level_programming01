#!/usr/bin/python3
# list all states in hbth_0e_0_usa in ascending order
from sys import argv
import MySQLdb
if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    con = MySQLdb.connect(user=username, passwd=password, db=dbname)
    cur = con.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall()]
