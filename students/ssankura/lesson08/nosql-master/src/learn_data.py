"""
    Lesson08 - Activity 01
    Author: Sireesha Sankuratripati
    Purpose: Extended the Data for database demonstrations - to split the "product" field into 2 fields - color & product_type
"""


def get_furniture_data():
    """
    demonstration data
    """

    furniture_data = [
        {
            'product_type': 'couch',
            'color': 'Red',
            'description': 'Leather low back',
            'monthly_rental_cost': 12.99,
            'in_stock_quantity': 10
        },
        {
            'product_type': 'couch',
            'color': 'Blue',
            'description': 'Cloth high back',
            'monthly_rental_cost': 9.99,
            'in_stock_quantity': 3
        },
        {
            'product_type': 'Coffee table',
            'color': 'Brown',
            'description': 'Plastic',
            'monthly_rental_cost': 2.50,
            'in_stock_quantity': 25
        },
        {
            'product_type': 'couch',
            'color': 'Red',
            'description': 'Leather high back',
            'monthly_rental_cost': 15.99,
            'in_stock_quantity': 17
        },
        {
            'product_type': 'recliner',
            'color': 'Blue',
            'description': 'Leather high back',
            'monthly_rental_cost': 19.99,
            'in_stock_quantity': 6
        },
        {
            'product_type': 'Chair',
            'color': 'Brown',
            'description': 'Plastic',
            'monthly_rental_cost': 1.00,
            'in_stock_quantity': 45
        },
        {
            'product_type': 'couch',
            'color': 'Black',
            'description': 'Leather high back',
            'monthly_rental_cost': 29.99,
            'in_stock_quantity': 6
        },
    ]
    return furniture_data
