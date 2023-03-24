#!/usr/bin/python3
"""safely filters the table against sql injections"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name = LIKE BINARY '{}'".format(argv[4]))
    [print(name) for name in cur.fetchall()]
