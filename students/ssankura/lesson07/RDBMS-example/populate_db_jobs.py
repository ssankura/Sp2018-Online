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
    logger.info('Creating Job records: just like Person. We use the foreign key')

    JOB_NAME = 0
    START_DATE = 1
    END_DATE = 2
    SALARY = 3
    PERSON_EMPLOYED = 4
    DEPT_EMPLOYED = 5

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30',65500, 'Andrew','C001'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew','C001'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew','C001'),
        ('Admin supervisor', '2012-10-01', '2014-11-10', 45900, 'Peter','A001'),
        ('Admin manager', '2014-11-14', '2018-01-05', 45900, 'Peter','A001')
        ]
    for job in jobs:
        logger.info(f'{job[JOB_NAME]} : {job[START_DATE]} to {job[END_DATE]} for salary {job[SALARY]} and person {job[PERSON_EMPLOYED]} in dept {job[DEPT_EMPLOYED]}')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for job in jobs:
            with database.transaction():
                new_job = Job.create(
                    job_name = job[JOB_NAME],
                    start_date = job[START_DATE],
                    end_date = job[END_DATE],
                    salary = job[SALARY],
                    person_employed = job[PERSON_EMPLOYED],
                    department_employed = job[DEPT_EMPLOYED]
                    )
                new_job.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed} in Department Number: {job.department_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_db()