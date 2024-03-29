#!/usr/bin/python3
"""
Find the id of a given state
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                 WHERE name LIKE BINARY '{}'".format(argv[4]))
    [print(name) for name in cur.fetchall()]
