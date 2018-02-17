"""
	Learning persistence with Peewee and sqlite
	delete the database to start over 
		(but running this program does not require it)
		
	need - logging
		- correct terminology
		- __main__
		- peewee create proper way
		- shell program - test and run
		- sqlite3 scripts
		
	Person:
		1. define data
		2. show connect
		3. insert records with logging
		4. display all records
		5. filter records and display
		6. add a new record
		7. delete a record

	Explanation
		1. Class = Table
		2. ? = Row
		3. ? = Column
		4. PK - business, numbers
		5. Introduce Jobs
		6. Diagram
		7. Normalization
		8. FK

	Job:	
		
"""

from personjob_model import *

def printu(message):
	print(f'---\n\n{message}')
	print('=' * len(message))

printu('PERSON')

PERSON_NAME = 0
LIVES_IN_TOWN = 1
NICKNAME = 2

people = [
	('Andrew', 'Sumner', 'Andy'),
	('Peter', 'Seattle', None),
	('Susan', 'Boston', 'Beannie'),
	('Pam', 'Coventry', 'PJ'),
	('Steven', 'Colchester', None),	
	]

printu('Creating Person records...')

for person in people:
    try:
        with database.transaction():
            new_person = Person.create(
                    person_name = person[PERSON_NAME],
                    lives_in_town = person[LIVES_IN_TOWN],
                    nickname = person[NICKNAME])
            new_person.save()

    except Exception as e:
        print(f'Error creating = {person[PERSON_NAME]}')
        print(e)

printu('Read and print all Person records we created...')

for person in Person:
	print(f'{person.person_name} lives in {person.lives_in_town} and likes to be known as {person.nickname}')

printu('Read and print by selecting the name of one Person name...')

aperson = Person.get(Person.person_name == 'Susan')
print(f'{aperson.person_name} lives in {aperson.lives_in_town} and likes to be known as {aperson.nickname}')


printu('Read and print by searching: look for missing nicknames')

for person in Person.select().where(Person.nickname == None):
	print(f'{person.person_name} does not have a nickname; see: {person.nickname}')
	if person.person_name == 'Peter':
		print('Changing nickname for Peter')
		person.nickname = 'Painter'
		person.save()
	else:
		print(f'Not giving a nickname to {person.person_name}')

aperson = Person.get(Person.person_name == 'Peter')
print(f'{aperson.person_name} now has a nickname of {aperson.nickname}')


printu('Add and display a Person called Fred; then delete him...')

new_person = Person.create(
	person_name = 'Fred',
	lives_in_town = 'Seattle',
	nickname = 'Fearless')
new_person.save()

aperson = Person.get(Person.person_name == 'Fred')

print(f'We just created {aperson.person_name}, who lives in {aperson.lives_in_town}')
print('but now we will delete him...')

aperson.delete_instance()

printu('Reading and print all Person records (but not Fred; he has been deleted)...')

for person in Person:
	print(f'{person.person_name} lives in {person.lives_in_town} and likes to be known as {person.nickname}')


printu('JOBS')

printu('Creating Jobs...')

JOB_NAME = 0 
START_DATE = 1
END_DATE = 2
SALARY = 3
PERSON_EMPLOYED = 4
	
jobs = [
	('Analyst', '2001-09-22', '2003-01-30',65500, 'Andrew'),
	('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew'),
	('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew'),
	('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Peter'),
	('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Peter')
	]

for job in jobs:
	try:
		with database.transaction():        
			new_job = Job.create(
				job_name = job[JOB_NAME],
				start_date = job[START_DATE],
				end_date = job[END_DATE],
				salary = job[SALARY],
				person_employed = job[PERSON_EMPLOYED])
			new_job.save()

	except Exception as e:
		print(f'Error creating = {job[JOB_NAME]}')
		print(e)

printu('Reading and print all Job rows (note the value of person)...')

for job in Job:
	print(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

printu('Now resolve the join and print (INNER shows only jobs that match person)...')

query = (Person
         .select(Person, Job)
         .join(Job, JOIN.INNER)
		)

for person in query:
	print(f'Person {person.person_name} had job {person.job.job_name}')

printu('Example of how to summarize data with a join(LEFT OUTER shows all, including no jobs)')
query = (Person
         .select(Person, fn.COUNT(Job.job_name).alias('job_count'))
         .join(Job, JOIN.LEFT_OUTER) 
         .group_by(Person)
         .order_by(Person.person_name))

for person in query:
    print(f'{person.person_name} had {person.job_count} jobs')
		

printu('Try to add a new job where a person doesnt exist...')

addjob = ('Sales', '2010-04-01', '2018-02-08', 80400, 'Harry')

try:
	with database.transaction():        
		new_job = Job.create(
				job_name = addjob[JOB_NAME], 
				start_date = addjob[START_DATE],
				end_date = addjob[END_DATE],
				salary = addjob[SALARY],
				person_employed = addjob[PERSON_EMPLOYED]) 
		new_job.save()
		
except Exception as e:
	print(f'For Job create: {addjob[0]}')
	print(e)

printu('Try to Delete a person who has jobs...')

try:
	with database.transaction():        
		aperson = Person.get(Person.person_name == 'Andrew')
		print(f'Trying to delete {aperson.person_name} who lives in {aperson.lives_in_town}')
		aperson.delete_instance()
		
except Exception as e:
	print(f'Delete failed: {aperson.person_name}')
	print(e)

printu('Creating Person records, but in a new table with generated PK...')

for person in people:
    try:
        with database.transaction():
            new_person = PersonNumKey.create(
                    person_name = person[PERSON_NAME],
                    lives_in_town = person[LIVES_IN_TOWN],
                    nickname = person[NICKNAME])
            new_person.save()

    except Exception as e:
        print(f'Error creating = {person[0]}')
        print(e)

printu('Creating Person records again in the new table with generated PK...')

for person in people:
    try:
        with database.transaction():
            new_person = PersonNumKey.create(
                    person_name = person[PERSON_NAME],
                    lives_in_town = person[LIVES_IN_TOWN],
                    nickname = person[NICKNAME])
            new_person.save()

    except Exception as e:
        print(f'Error creating = {person[0]}')
        print(e)

printu('Note no PK specified, no PK violation; "duplicates" created!')		

for person in PersonNumKey.select():
	print(f'Name : {person.person_name} with id: {person.id}')
	
printu('Try to change the name of a Person...')

aperson = Person.get(Person.person_name == 'Peter')
print(f'Curent value is {aperson.person_name}')

printu('Update Peter to Peta, thereby trying to change the PK...')

try:
	with database.transaction():
		aperson = Person.get(Person.person_name == 'Peter')
		aperson.person_name = 'Peta'
		aperson.save()
		print(f'Tried to change Peter to {aperson.person_name}')
		
except Exception as e:
	print(f'Cant change a PK and caught you trying') # not caught; no error thrown by Peewee
	print(e)

aperson = Person.get(Person.person_name == 'Peter')
print(f'Looked for Peter: found! -> {aperson.person_name}')

try:
	aperson = Person.get(Person.person_name == 'Peta')

except Exception as e:
	print(f'Looking for Peta results in zero records. PK changes are ignored and do not throw an error!!!!')
	print(f'Cant change a PK')
	print('PK "change" can only be achieved with a delete and new create')

printu('DONE!')

database.close()
