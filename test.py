import mysql.connector

db = mysql.connector.connect(
	host = "172.0.0.1",
	user = "lamhot",
	passwd = "lamhot",
	database = "testdatabase"

)

mycursor = db.cursor()