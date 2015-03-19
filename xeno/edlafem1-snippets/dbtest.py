import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', database='employees', host='localhost')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT first_name, last_name FROM employees LIMIT 10")


for first_name, last_name in cursor:
    print("First name: {0}, Last name: {1}").format(first_name, last_name)