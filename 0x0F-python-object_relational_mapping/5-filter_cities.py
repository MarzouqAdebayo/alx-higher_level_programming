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

    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>"
            .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database)
        cur = conn.cursor()

        # Using parameterized query to prevent SQL injection
        query = """
        SELECT DISTINCT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
        """
        cur.execute(query, (state_name,))

        rows = cur.fetchall()

        n = len(rows)
        if (n == 0):
            print("")
        for i in range(n):
            if (i == n - 1):
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)
