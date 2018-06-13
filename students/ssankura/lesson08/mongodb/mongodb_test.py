"""
    Mongodb #1
    test and learn mongodb
    for this to work in macos you must run from bash:
        open "/Applications/Python 3.6/Install Certificates.command"

"""
# code intentionally omitted - see git for complete module

    logger.info('Setup the connection to mongodb')
    with src.login_database.login_mongodb_cloud() as client:

        logger.info('We are going to use a database called dev')
        db = client['dev']

        logger.info('And in that database create a collection called furniture')

        furniture = db['furniture']

        logger.info('Now we add data from the dictionary')
        results = furniture.insert_many([
        {
            'product': 'Red couch',
            'in_stock_quantity': 10
        },
        {
            'product': 'Blue couch',
            'in_stock_quantity': 3
        }])

        logger.info('Find the products that are described as plastic')
        query = {'product': 'Red couch'}
        results = furniture.find_one(query)

if __name__ == '__main__':
    main()