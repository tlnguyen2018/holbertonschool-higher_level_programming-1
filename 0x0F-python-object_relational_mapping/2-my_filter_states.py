#!/usr/bin/python3

""" lists all states from given argument """


from sys import argv
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()
    cursor.execute("""SELECT * FROM states WHERE BINARY name = '{}'
                   ORDER BY id ASC""".format(argv[4]))
    rows = cursor.fetchall()
    for x in rows:
        print(x)
    cursor.close()
    database.close()
