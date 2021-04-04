import os
import mysql.connector as database
import sys
from config import DB_NAME, DB_ADMIN, DB_PASSWORD, DB_HOST

# Check user is entered before conencting
if len(sys.argv) != 2:
    print("USAGE: %s <username>" % sys.argv[0])
    sys.exit(1)

connection = database.connect(
    user = DB_ADMIN,
    password = DB_PASSWORD,
    host = DB_HOST,
    database = DB_NAME)

username = sys.argv[1]
cursor = connection.cursor()

cursor.execute("DELETE FROM users WHERE username = %s;", (username,))
connection.commit()

print("* User '%s' successfully removed" % username)
connection.close()
