#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mysql.connector as database
import sys
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

ovpnuser = os.environ['username']

cursor.execute('SELECT * FROM users WHERE username = ?;', (os.environ['username'],))
result = cursor.fetchone()

if result is None:
    sys.exit(1)
username, password = result
passw = (os.environ['password'] + salty) #Salt this mofo
if hash_func(passw.encode("utf-8")).hexdigest() != password:
    sys.exit(1)
sys.exit(0)
