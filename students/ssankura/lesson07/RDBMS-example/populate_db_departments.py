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

    logger.info('Working with Department class')
    logger.info('Creating Department records: just like Person. ')
    
    DEPT_NUM = 0
    DEPT_NAME = 1
    DEPT_MGR_NAME = 2

    departments = [
        ('C001', 'Cloud Computing1', 'Jane Austen'),
        ('A001', 'Accounting', 'Andrew Smith'),
        ('C002', 'Cloud Computing2', 'Bob Madson'),
        ('S001', 'Security Cloud', 'Peter Schneider'),
        ('S002', 'Security Applications', 'Amy Watson')
        ]

    try:
        logger.info("Printing Department that will be inserted into the DB")
        #for dept in departments:
        #    logger.info (f'{dept[DEPT_NUM]}, {dept[DEPT_NAME]} , {dept[DEPT_MGR_NAME]}')
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in departments:
            dept_num = dept[DEPT_NUM]
            dept_name = dept[DEPT_NAME]
            dept_mgr = dept[DEPT_MGR_NAME]
            logger.info (f'Creating Department Record with data = [{dept_num}, {dept_name}, {dept_mgr}]')
            with database.transaction():
                new_dept = Department.create(
                    department_number = dept_num,
                    department_name = dept_name,
                    department_manager_name = dept_mgr)
                new_dept.save()


        logger.info('Reading and print all Department rows (note the value of department)...')
        for dept in Department:
            logger.info(f'{dept.department_number} , {dept.department_name} ')
            #logger.info(f'{dept.department_number} , {dept.department_name}, {dept.department_manager_name} ')

    except Exception as e:
        logger.info(f'Error creating record = [{dept[DEPT_NUM]}, {dept[DEPT_NAME]}, {dept[DEPT_MGR_NAME]}]')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_db()