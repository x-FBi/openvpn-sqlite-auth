Edit db.php:
'''
$db = new PDO('sqlite:database.name'); make database.name reflect your config.py settings.
'''

edit index.php: 
'''
$saltysalt = hash('sha512',"t0p$eCRT"); # EDIT ME
'''
