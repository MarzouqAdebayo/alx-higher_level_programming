#!/usr/bin/python3
"""
Create states table in hbtn_0e_0_usa with some data
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC;"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
