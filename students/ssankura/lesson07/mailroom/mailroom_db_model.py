import logging
from peewee import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

class BaseModel(Model):
	class Meta:
		database = database

class Donor(BaseModel):
	logger.info ("Donor Object")
	donor_name = CharField (primary_key = True, max_length = 50)
	donor_lives_in = CharField(max_length = 40, null = False)

class Donation(BaseModel):
	logger.info("Donation Object")
	donation_amount = DecimalField(max_digits=9, decimal_places=2)
	donation_date = DateField(formats = 'MM-DD-YYYY', null = True)
	donated_by = ForeignKeyField(Donor, related_name = 'donor', null = False)

database.create_tables([Donor, Donation])

database.close()