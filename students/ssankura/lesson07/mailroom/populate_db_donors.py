import logging
from peewee import *
from mailroom_db_model import *

def populate_db():
	"""
		add donors to database
	"""

	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger(__name__)

	database = SqliteDatabase('mailroom.db')

	logger.info('Working with Mailroom class')
	logger.info('Creating Donor records: ')

	DONOR_NAME = 0
	LIVES_IN_TOWN = 1

	donors = [('Mark Zuckerberg', 'San Francisco'),
		('Jeff Bezos', 'Seattle'),
		('William Gates','Seattle'),
		('J K Rowling','London')
		]

	try:
		database.connect()
		database.execute_sql('PRAGMA foreign_keys = ON;')
		for donor in donors:
			with database.transaction():
				new_donor = Donor.create(
                    donor_name = donor[DONOR_NAME],
    			    donor_lives_in = donor[LIVES_IN_TOWN]
    			    )
				new_donor.save()

		logger.info('Reading and print all donors')
		for donor in Donor:
			logger.info(f'{donor.donor_name} , {donor.donor_lives_in}')
	
	except Exception as e:
		logger.info (f'Error creating Donor [{donor[DONOR_NAME]}]')
		logger.info(e)

	finally:
		logger.info ('database closes')
		database.close()

if __name__ == '__main__':
    populate_db()

