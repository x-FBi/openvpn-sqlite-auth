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
DB = "CREATE DATABASE IF NOT EXISTS %s" % DB_NAME # Create database, unless it exists

try:
    cursor.execute(DB)
    print(f"* Created Database %s" % DB_NAME)
except database.Error as e:
    print(f"Error Creating Database: {e} ")
    sys.exit
