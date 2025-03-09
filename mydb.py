import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'suresh',
	)

# prepare a cursor object

Cursorobject = database.cursor()

# create a database
Cursorobject.execute("CREATE DATABASE dbcrm")
print("ALL DONE;")
