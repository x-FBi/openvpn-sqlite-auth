#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import sqlite3
import sys
from getpass import getpass

from config import DB_PATH, PASSWORD_LENGTH_MIN, HASH_ALGORITHM, HASH_SALTY


if len(sys.argv) != 2:
    print("USAGE: %s <username>" % sys.argv[0])
    sys.exit(1)
if not os.path.exists(DB_PATH):
    print("ERROR: Database not found: %s" % DB_PATH)

hash_func = getattr(hashlib, HASH_ALGORITHM, None)
if hash_func is None:
    print("ERROR: Hashing algorithm '%s' not found" % HASH_ALGORITHM)
    sys.exit(2)

username = sys.argv[1]
password_ok = False

db = sqlite3.connect(DB_PATH)
cursor = db.cursor()
try:
    cursor.execute("SELECT COUNT(*) as count FROM users WHERE username = (?);", (username,))
    user = cursor.fetchone()
    ucount = user[0]
    if ucount == 1:
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
        cursor.execute("UPDATE users SET password = (?) WHERE username = (?);", (password, username))
    else:
        print("Error: User '%s' was not found" % username)
        sys.exit(2)

except sqlite3.IntegrityError:
    print("ERROR")
    sys.exit(2)

db.commit()
print("* User %s password successfully updated" % username)
