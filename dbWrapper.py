__author__ = 'lukez'

import _mysql

def main():
    try:
        connection = _mysql.connect('localhost', 'lukezim5', 'zim865', 'megs')
        connection.query("SELECT VERSION()")
        result = connection.use_result()

        print("MySQL version: %s" % \
        result.fetch_row()[0])
    except _mysql.Error as err:
        print(err)
    connection.close()

main()