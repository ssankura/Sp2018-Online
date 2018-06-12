"""
    Lesson08 - Activity01
    Author: Sireesha Sankuratripati
    Pupose: Extended the mongodb example to change the input data format and aggregate/print data based on new input format
"""

import pprint
import login_database
import utilities
import pymongo

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_example(furniture_items):
    """
    mongodb data manipulation
    """
    log.info("*** START MONGO DB SCRIPT ****")
    client = login_database.login_mongodb_cloud()

    log.info('Step 1: We are going to use a database called dev')
    log.info('But if it doesnt exist mongodb creates it')
    db = client.dev

    log.info('And in that database use a collection called furniture')
    log.info('If it doesnt exist mongodb creates it')

    furniture = db.furniture

    log.info('Step 2: Now we add data from the dictionary above')
    furniture.insert_many(furniture_items)

    log.info('Step 3: Find the products that are described as plastic')
    query = {'description': 'Plastic'}
    results = furniture.find(query)
    pprint.pprint(results)
    log.info('Step 4: Print the plastic products')
    for row in results:
        log.info (f" Product: {row['color']} {row['product_type']}, Description: {row['description']}, Monthly Rental: {row['monthly_rental_cost']}, In Stock Qty: {row['in_stock_quantity']}")    

    log.info('Step 5: Delete the blue couch (actually deletes all blue couches)')
    furniture.remove( { "$and": [ {"product_type": "couch"}, {"color": "Blue"} ] })

    log.info('Step 6: Check it is deleted with a query and print')
    query = {'product': 'Blue couch'}
    results = furniture.find_one({ "$and": [ {"product_type": "couch"}, {"color": "Blue"} ] })

    log.info('The blue couch is deleted, print should show none:')
    log.info(results)

    log.info ('Step 6.1 : print all data after deleting Blue couch')
    results = furniture.find({})
    for row in results:
        log.info (f" Product: {row['color']} {row['product_type']}, Description: {row['description']}, Monthly Rental: {row['monthly_rental_cost']}, In Stock Qty: {row['in_stock_quantity']}")
    
    log.info(
        'Step 7: Find multiple documents, iterate though the results and print products whose rental > 15.00')

    cursor = furniture.find({"monthly_rental_cost": {"$gte": 15.00}})
    print('Results of search')
    log.info('Notice how we parse out the data from the document')
    for doc in cursor:
        log.info (f"Product: {doc['color']} {doc['product_type']}, Description: {row['description']}, Rental Cost: {doc['monthly_rental_cost']}, In Stock Qty: {doc['in_stock_quantity']}")

    log.info('Step 8: Find all products where color = Red')
    cursor = furniture.find({"$or" :[{"color": 'red'},{'color':'Red'},{'color':'RED'}]})
    print('Results of search:')
    for doc in cursor:
        log.info (f"Product: {doc['color']} {doc['product_type']}, Description: {row['description']}, Rental Cost: {doc['monthly_rental_cost']}, In Stock Qty: {doc['in_stock_quantity']}")

    log.info('Step 9: Find all products where type = couch')
    cursor = furniture.find({"$or" :[{"product_type": 'couch'},{'product_type':'Couch'},{'product_type':'COUCH'}]})
    log.info('Results of search:')
    for doc in cursor:
        log.info (f"Product: {doc['color']} {doc['product_type']}, Description: {row['description']}, Rental Cost: {doc['monthly_rental_cost']}, In Stock Qty: {doc['in_stock_quantity']}")


    log.info('Step 10: Delete the collection so we can start over')
    db.drop_collection('furniture')
    log.info("*** END MONGO DB SCRIPT ****")

