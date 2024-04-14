#!/usr/bin/python3
"""
Create states table in hbtn_0e_0_usa with some data
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state_name>"
                .format(sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
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
