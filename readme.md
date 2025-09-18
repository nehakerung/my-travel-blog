# My Travel Blog
This is a travel blog used to showcase my personal travels. It uses a django framework and mysql database.

## How to run locally
### Pre-requisites
1. Python
2. Pyenv
3. mysql

### Clone repo
```
git clone

poetry install
```
### Set up MySQL database
(While in development)
```
mysql -u root

mysql> 
    CREATE DATABASE mydb CHARACTER SET UTF8;
	CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypassword';
	GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%';
	FLUSH PRIVILEGES;
```

```
make dev-init

poetry run python manage.py createsuperuser --username admin --email admin@example.com --password changeme

```
### Linters
```
make lint
```

Edittt