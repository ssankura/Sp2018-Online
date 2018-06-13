"""
    Lesson 08 - Activity 01
    Author: Sireesha Sankuratripati
    Purpose: Extended the neo4j example to add additional person rows, add colors and define person-fav color relationsips 
                and to print the person-favorite colors relationships
"""


import utilities
import login_database
import utilities
import random

log = utilities.configure_logger('default', '../logs/neo4j_script.log')


def run_example():
    log.info("*** START NEO4J SCRIPT ****")

    log.info('Step 1: First, clear the entire database, so we can start over')
    log.info("Running clear_all")

    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    log.info("Step 2: Add a few people")

    with driver.session() as session:
        colors =[]
        people = []

        log.info('Adding a few Person nodes')
        log.info('The cyph language is analagous to sql for neo4j')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ('Sireesha','Sankuratripati'),
                            ('William','Gates')
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)

        log.info("Step 3: Get all of people in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result_people = session.run(cyph)
        print("People in database:")

         #storing people in a list as tuples for easy access - cursor will get closed after a read
        for record in result_people:
            tmp_first_name = record['first_name']
            tmp_last_name = record['last_name']
            name_tuple = (tmp_first_name, tmp_last_name)
            people.append (name_tuple)
        print (people)

        log.info("Step 4: Adding some colors in the DB:")
        for color in [('Pink'),('Blue'),('Black'),('Yellow'),('Green'),('Red'),('White')]:
            clr_cyph = "CREATE (n:Color {color_name:'%s'})" %(color)
            session.run (clr_cyph)
        
        log.info("Step 5: Get all of colors in the DB:")

        cyph = """MATCH (c:Color)
                  RETURN c.color_name as color
                """
        result_colors = session.run(cyph)

        #storing colors in a list for easy access - cursor will get closed after a read
        log.info("Colors in database:")
        for record in result_colors:
            tmp_color = record['color']
            colors.append (tmp_color)
        print (colors)
        log.info('Step 6: Create some relationships - People and Colors')
    
        #Add two favorite colors for each person with the outer for loop - picking a random color each time 
        for i in range(0,2):
            for tuple_name in people:
                tmp_first_name = tuple_name[0]
                tmp_last_name = tuple_name[1]
                tmp_color = random.choice(colors)
                log.info (f"Adding Favorite color for {tmp_first_name} {tmp_last_name} as {tmp_color}")
                cyph = "MATCH (p1:Person {first_name:'%s', last_name:'%s'})" %(tmp_first_name, tmp_last_name)
                cyph += "CREATE (p1)-[fav:FAVORITE]->(p2:Color {color:'%s'})" %(tmp_color)
                cyph += "RETURN p1"
                session.run (cyph)


        log.info('Step 7: Print the relationships - the favorite colors for ALL the People')
        # Get and print favorite colors for each person
        for person_tuple in people:
            cyph = "MATCH (person {first_name:'%s', last_name:'%s'})-[:FAVORITE]->(personFavs) RETURN personFavs" %(person_tuple[0], person_tuple[1])
            result_fav_colors = session.run (cyph)

            message_person = f"Favorite colors for {person_tuple[0]} {person_tuple[1]} are :"
            for record in result_fav_colors:
                for color_row in record.values():
                    message_person += f" {color_row['color']},"
            log.info (message_person[:-1]) #strip the last comma

        log.info('Step 8: Create some relationships - Friends')
        log.info("Bob Jones likes Alice Cooper, Fred Barnes and Marie Curie")

        for first, last in [("Alice", "Cooper"),
                            ("Fred", "Barnes"),
                            ("Marie", "Curie")]:
            cypher = """
              MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        log.info("Step 9: Find all of Bob's friends")
        cyph = """
          MATCH (bob {first_name:'Bob', last_name:'Jones'})
                -[:FRIEND]->(bobFriends)
          RETURN bobFriends
          """
        result = session.run(cyph)
        print("Bob's friends are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])

        log.info("Setting up Marie's friends")

        for first, last in [("Mary", "Evans"),
                            ("Alice", "Cooper"),
                            ('Fred', 'Barnes'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'Marie', last_name:'Curie'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)

            session.run(cypher)

        print("Step 10: Find all of Marie's friends?")
        cyph = """
          MATCH (marie {first_name:'Marie', last_name:'Curie'})
                -[:FRIEND]->(friends)
          RETURN friends
          """
        result = session.run(cyph)
        print("\nMarie's friends are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])
    log.info("*** END NEO4J SCRIPT ****")

if __name__ == '__main__':
    run_example()
