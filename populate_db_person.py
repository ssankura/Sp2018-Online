"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

from personjob_model import *

import logging

def populate_db():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Job class')
    logger.info('Creating Person records: ')

    PERSON_NAME = 0
    LIVES_IN_TOWN = 1
    NICKNAME = 2
   
    persons = [
        ('Andrew', 'Boston', ''),
        ('Peter', 'Seattle', '')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for person in persons:
            with database.transaction():
                new_person = Person.create(
                    person_name = person[PERSON_NAME],
                    lives_in_town = person[LIVES_IN_TOWN],
                    nickname = person[NICKNAME]
                    )
                new_person.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for person in Person:
            logger.info(f'{person.person_name} , {person.lives_in_town} , {person.nickname}')

    except Exception as e:
        logger.info(f'Error creating = {person[person_name]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_db()