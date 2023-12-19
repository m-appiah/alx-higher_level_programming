#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Retrieving username, password, and database name
    from command line arguments
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()
    """Create a cursor object"""

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
