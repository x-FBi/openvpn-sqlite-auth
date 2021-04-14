import os
import mysql.connector as database
import sys
from config import DB_NAME, DB_ADMIN, DB_PASSWORD, DB_HOST

connection = database.connect(
    user = DB_ADMIN,
    password = DB_PASSWORD,
    host = DB_HOST,
    database = DB_NAME)

cursor = connection.cursor()

try:
     cursor.execute("SELECT usernames FROM users;")
     users = cursor.fetchall()
     print("*** OpenVPN access list:")
     for user in users:
        print(" - %s" % user)
except database.Error as e:
     print(f"Error retrieving entry from database: {e}")

connection.close()
