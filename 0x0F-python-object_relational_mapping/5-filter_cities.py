#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa by state
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

    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    cities = ', '.join([row[0] for row in rows])
    print(cities)
