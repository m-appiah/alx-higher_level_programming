#!/usr/bin/python3
"""
Displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()

    cursor.execute(
            "SELECT id, name FROM states WHERE name = '{0}' ORDER BY id".formt(
                argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
