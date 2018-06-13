"""
    Lesson 08 - Activity 01
    Author: Sireesha Sankuratripati
    Purpose: Extended the example for Usage of Redis to store customer data as a list with a key as customer id (name, phone, email and zipcode)
                adding 6 customers with the new data fields, printing the customer(s) data 
                and deleting each newly added customer from Redis Cache (all list items for each customer)
"""


import login_database
import utilities

log = utilities.configure_logger('default', '../logs/redis_script.log')
r = login_database.login_redis_cloud()

def get_print_cust_data(person_key):
    log.info (f"Customer Name: {r.lindex(person_key,0)}, Phone: {r.lindex(person_key,1)}, Email Id: {r.lindex(person_key,2)}, ZipCode: {r.lindex(person_key,3)}")

def rem_cust_data(person_key):
    person_name = r.lindex(person_key,0)
    person_phone = r.lindex(person_key,1)
    person_email = r.lindex(person_key,2)
    person_zipcode = r.lindex(person_key,3)
    log.info (f" Customer: {person_name}, Count of list items in Redis Cache before deletion: {r.llen(person_key)}")

    r.lrem(person_key,0,person_name)
    r.lrem(person_key,0,person_phone)
    r.lrem(person_key,0,person_email)
    r.lrem(person_key,0,person_zipcode)
    log.info (f" Customer: {person_name}, Count of list items in Redis Cache after deletion: {r.llen(person_key)}")


def run_example():
    """
        uses non-presistent Redis only (as a cache)
    """
    try:
        log.info("*** START REDIS SCRIPT ****")

        log.info('****Step 1: connect to Redis')
        log.info('Step 2: cache some data in Redis')
        r.rpush('c1', 'andy', '510-909-1575','andy@somewhere.com',77598)

        log.info('Step 2: now I can read data for first customer')
        get_print_cust_data('p1')

        log.info('Step 3: Cache data for more five more customers in Redis')
        r.rpush('c2','pam',  '650-981-1872','pam@somewhere.com',85286)

        r.rpush('c3', 'fred', '480-891-2534','fred@fearless.com',85226)
        r.rpush('c4', 'bob', '310-671-0912','bob@mail.com',57651)
        r.rpush('c5', 'amanda', '210-982-8145','amanda@somemail.com',10025)
        r.rpush('c6', 'jennifer', '623-450-9810','jennifer@somemail.com',87901)
        log.info('Step 4: now I can read data for five more customers')

        get_print_cust_data('c2')
        get_print_cust_data('c3')
        get_print_cust_data('c4')
        get_print_cust_data('c5')
        get_print_cust_data('c6')


        log.info('Step 5: delete all customer data from cache')
        rem_cust_data('c1')
        rem_cust_data('c2')
        rem_cust_data('c3')
        rem_cust_data('c4')
        rem_cust_data('c5')
        rem_cust_data('c6')

        log.info(
            'Step 6: Redis can maintain a unique ID or count very efficiently')
        r.set('user_count', 21)
        r.incr('user_count')
        r.incr('user_count')
        r.decr('user_count')
        result = r.get('user_count')
        log.info('I could use this to generate unique ids')
        log.info(f'Redis says 21+1+1-1={result}')

        log.info('Step 7: richer data for a SKU')
        r.rpush('186675', 'chair')
        r.rpush('186675', 'red')
        r.rpush('186675', 'leather')
        r.rpush('186675', '5.99')

        log.info('Step 8: pull some data from the structure')
        cover_type = r.lindex('186675', 2)
        log.info(f'Type of cover = {cover_type}')

    except Exception as e:
        print(f'Redis error: {e}')
    finally:
        log.info("*** END REDIS SCRIPT ****")


if __name__ == '__main__':
    run_example()
