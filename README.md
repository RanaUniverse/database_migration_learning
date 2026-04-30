# What this project is for?

This repo i made to test the database migration tool ie, `alembic`, how to use this and for like this things i make this repo for testing.

I will try to use and test `postgres` database with the python libraries.
I will try to use the docs of `sqlmodel` to get and work with demo data of the database.

##
How to use the postgres database
`sudo systemctl start postgresql`
It will start the postgres service which is need to talk to postgres database by the python code.

### How i will make the database before:
```bash
rana@laptop:~$ sudo -iu postgres
postgres@laptop:~$ psql
psql (18.3 (Ubuntu 18.3-1.pgdg24.04+1))
Type "help" for help.

postgres=# CREATE DATABASE hero1 owner rana;
CREATE DATABASE
postgres=# \c
You are now connected to database "postgres" as user "postgres".
postgres=# \list
postgres=# \l
postgres=# 
```