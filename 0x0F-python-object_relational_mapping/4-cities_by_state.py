#!/usr/bin/python3
"""
a script that takes in an argument and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database>"
            .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database)
        cur = conn.cursor()

        # Using parameterized query to prevent SQL injection
        query = """
        SELECT cities.id, cities.name, states.name
        FROM states INNER JOIN cities
        ON cities.state_id = states.id
        ORDER BY cities.id;
        """
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)
