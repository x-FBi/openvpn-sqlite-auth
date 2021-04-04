# -*- coding: utf-8 -*-

# Name of the database where usernames will be stored
DB_NAME = 'users'
# SQL user
DB_ADMIN = 'admin'
# SQL user password
DB_PASSWORD = 'password1'
# SQL Host
DB_HOST = '127.0.0.1'
# Minimum required length for passwords when creating users
PASSWORD_LENGTH_MIN = 5
# Hash algorithm to use for passwords storage. Can be one of:
# md5, sha1, sha224, sha256, sha384, sha512
HASH_ALGORITHM = 'sha512'
# Add a SALT to the password.  Change SALT accordingly
HASH_SALTY = 't0p_$Ecr3t!'
