#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mysql.connector as database
import sys
from config import DB_NAME, DB_ADMIN, DB_PASSWORD, DB_HOST

connection = database.connect(
    user=DB_ADMIN,
    password=DB_PASSWORD,
    host=DB_HOST,
)
cursor = connection.cursor()

try:
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)
        if x == DB_NAME:
            print(f"Database %s Already Exists" % DB_NAME)
            sys.exit
except database.Error as e:
    print(f"Error:  {e} ")
    sys.exit

try:
    print(f"CREATE DATABASE %s;" % DB_NAME)
    cursor.execute("create database if not exists %s", (DB_NAME, ))
    print(f"* Created Database %s" % DB_NAME)
except database.Error as e:
    print(f"Error Creating Database: {e} ")
    sys.exit
