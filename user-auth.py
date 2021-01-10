#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import sqlite3
import sys

from config import DB_PATH, HASH_ALGORITHM, HASH_SALTY


hash_func = getattr(hashlib, HASH_ALGORITHM)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
salty = hash_func(HASH_SALTY.encode("utf-8")).hexdigest()

cursor.execute('SELECT * FROM users WHERE username = ?;', (os.environ['username'],))
result = cursor.fetchone()
if result is None:
    sys.exit(1)
username, password = result
passw = (os.environ['password'] + salty) #Salt this mofo
if hash_func(passw.encode("utf-8")).hexdigest() != password:
    sys.exit(1)
sys.exit(0)
