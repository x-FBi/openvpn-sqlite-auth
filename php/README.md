# Update User Password Setup

Place both files in your /var/www/  folder

## Edit db.php:
```
$db = new PDO('sqlite:database.name'); 
```
make database.name reflect your config.py settings.


## Edit index.php: 
```
$saltysalt = hash('sha512',"t0p$eCRT"); # EDIT ME
```
make "topSecret" reflect your config.py settings

## Database Read-Only

If you get a read only error when updating a password, you may need to do the following

```
sudo chown -R :www-data /etc/openvpn/database/
sudo chmod -R 775 /etc/openvpn/database
```
