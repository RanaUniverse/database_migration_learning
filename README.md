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

# What to do with alembic,

```
alembic revision --autogenerate -m "initial migration first time"
```
Thsi will generate the some files in the alembic/versions/*py file.
```
alembic upgrade head
```
This will do changes the structer of the database and from then i will able to add new data in the database.

then i will change the model in my code and do follow the upper things again.

`cascade=true` this will apply in the Relationship field, but the `ondelete=``CASCADE`/`SET NULL`/`RESTRICT` > these are says for database level when anyone want to contact with real database only with sql query.
Examples:
    this is very risky to use ondelete=cascade
```
class Hero():
    team_id:in|None = Field(default=None, foreign_key="team.id", ondelete="CASCADE")
class Team(SQLModel, table=True):
    heroes: list[Hero] = Relationship(cascade_delete=True)
```
