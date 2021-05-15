#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mysql.connector as database
import sys
import hashlib
from config import DB_NAME, DB_ADMIN, DB_PASSWORD, DB_HOST, HASH_ALGORITHM, HASH_SALTY

connection = database.connect(
    user=DB_ADMIN,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME
)
cursor = connection.cursor()


hash_func = getattr(hashlib, HASH_ALGORITHM)
salty = hash_func(HASH_SALTY.encode("utf-8")).hexdigest()

#ovpnuser = (os.environ['username'])
ovpnuser = os.environ.get('username', 'test') # ovpn uses 'username'  and 'test' is default if not found
ovpnuser = "SELECT * FROM users WHERE usernames = '" + ovpnuser + "';"
print(ovpnuser)
cursor.execute(ovpnuser)
result = cursor.fetchone()

if result is None:
    print(f"No User Found in: " + ovpnuser + " \n")
    sys.exit(1)

id, usernames, passwords = result
passw = (os.environ.get('password') + salty) #Salt this mofo
#passw = (os.environ['password'] + salty) #Salt this mofo
#print(passwords)
#print(passw)
f = open('/root/auth-error.log', 'a')
f.write("passwords: " + passwords)
f.write("\npassw: " + passw)
f.write("\nEncoded: " + hash_func(passw.encode("utf-8")).hexdigest() + "\n")
f.close()
if hash_func(passw.encode("utf-8")).hexdigest() != passwords:
    print(f"DENIED: " + passw)
    sys.exit(1)

print(f"Success!")
sys.exit(0)
