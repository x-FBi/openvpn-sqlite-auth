#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import mysql.connector as database
import sys
from getpass import getpass
from config import PASSWORD_LENGTH_MIN, HASH_ALGORITHM, HASH_SALTY, DB_NAME, DB_ADMIN, DB_PASSWORD, DB_HOST

if len(sys.argv) != 2:
    print("USAGE: %s <username>" % sys.argv[0])
    sys.exit(1)

hash_func = getattr(hashlib, HASH_ALGORITHM, None)
if hash_func is None:
    print("ERROR: Hashing algorithm '%s' not found" % HASH_ALGORITHM)
    sys.exit(2)

username = sys.argv[1]
password_ok = False
while not password_ok:
    password = getpass()
    if len(password) < PASSWORD_LENGTH_MIN:
        print("ERROR: password must be at least %d characters long" % PASSWORD_LENGTH_MIN)
        continue
    password_confirm = getpass('Confirm: ')
    if password == password_confirm:
        password_ok = True
    else:
        print("ERROR: passwords don't match")

salty = hash_func(HASH_SALTY.encode("UTF-8")).hexdigest()
password = password + salty
password = hash_func(password.encode("UTF-8")).hexdigest()

connection = database.connect(
    user = DB_ADMIN,
    password = DB_PASSWORD,
    host = DB_HOST,
    database = DB_NAME
)

au = "INSERT INTO users VALUES %s, %s;"  %(username, password)
print(au)
cursor = connection.cursor()
try:
    cursor.execute("REPLACE INTO users(usernames, passwords) VALUES (%s, %s);", (username, password))
except database.IntegrityError as e:
    print(f"ERROR: ".format(e))
    sys.exit(2)

connection.commit()
print(f"* User %s successfully created" % username)
