"""
	Simple database examle with Peewee ORM, sqlite and Python

"""

from peewee import *

# connect to sqlite database
# database is created if it doesnt exist

sqlite_db = SqliteDatabase('personjob.db')

