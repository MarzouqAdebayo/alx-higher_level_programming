#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cur = connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY `id` ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()
