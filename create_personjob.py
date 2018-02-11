"""
	Create database examle with Peewee ORM, sqlite and Python

"""

from personjobdb import *

database.connect()

database.create_tables([
        Job,
        Person
    ])

database.close()
