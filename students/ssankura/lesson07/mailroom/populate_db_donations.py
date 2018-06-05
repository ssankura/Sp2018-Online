import logging
from peewee import *
from mailroom_db_model import *

def populate_db():
    """
        add donations to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    logger.info('Working with Mailroom class')
    logger.info('Creating Donation records: ')

    DONATION_AMT = 0
    DONATION_DATE = 1
    DONOR_NAME = 2


    #donation_amount = DecimalField(max_digits=7, decimal_places=2)
    #donation_date = DateField(formats = 'MM-DD-YYYY')
    #donated_by = ForeignKeyField(Donor, related_name = 'donor', null = False)

    donations = [
        (10000.05, '05-01-2017', 'Mark Zuckerberg'),
        (29000.95, '09-01-2017', 'Mark Zuckerberg'),
        (129000.95, '09-01-2018', 'Jeff Bezos'),
        (50150.50,'09-20-2017', 'J K Rowling'),
        (5000.50,'07-15-2017', 'William Gates'),
        (150000.50,'07-15-2017', 'William Gates'),
        (250150.50,'09-20-2017', 'J K Rowling'),
        (329000.95, '09-01-2017', 'Jeff Bezos'),
        (10000.00, '01-01-2018', 'Jeff Bezos'),
        (13000.00, '11-01-2017', 'Mark Zuckerberg')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donor = Donation.create(
                    donation_amount = donation[DONATION_AMT],
                    donation_date = donation[DONATION_DATE],
                    donated_by = donation[DONOR_NAME]
                    )
                new_donor.save()

        logger.info('Reading and print all donors')
        for donation in Donation:
            logger.info(f'{donation.donation_amount} , {donation.donation_amount}, {donation.donated_by}')

    except Exception as e:
        logger.info (f'Error creating Donation : [{donation[DONATION_AMT]} , {donation[DONATION_DATE]}, {donation[DONOR_NAME]}]')
        logger.info(e)

    finally:
        logger.info ('database closes')
        database.close()

if __name__ == '__main__':
    populate_db()

