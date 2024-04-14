#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database)
    cur = connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY `id` ASC;")
    rows = cur.fetchall()
    for row in rows:
        if (row[1][0] == "N"):
            print(row)
    cur.close()
    connection.close()
