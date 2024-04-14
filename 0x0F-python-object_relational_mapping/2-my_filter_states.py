#!/usr/bin/python3
"""
Create states table in hbtn_0e_0_usa with some data
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cur = connection.cursor()
        cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC;"
                    .format(state_name))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)
