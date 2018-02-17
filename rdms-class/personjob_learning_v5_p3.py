"""
	Learning persistence with Peewee and sqlite
	delete the database to start over 
		(but running this program does not require it)
		
		
"""

from personjob_model import *

JOB_NAME = 0 
START_DATE = 1
END_DATE = 2
SALARY = 3
PERSON_EMPLOYED = 4

logger.info('View matching records and Persons without Jobs (note LEFT_OUTER)')

query = (Person
         .select(Person, Job)
         .join(Job, JOIN.LEFT_OUTER)
        )

for person in query:
    logger.info(f'Person {person.person_name} had job {person.job.job_name}')

database.close()
