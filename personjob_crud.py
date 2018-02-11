"""
	Learning persistence with Peewee and sqlite

"""

from personjobdb import *

database.connect()

print('PERSON')

people = [
	('Andrew', 'Sumner', 'Andy'),
	('Peter', 'Seattle',''),
	('Susan', 'Boston', 'Beannie'),
	('Pam', 'Coventry', 'PJ')	
	]

print ('Creating Persons...')
# add error check here for pk violation
for person in people:
	new_person = Person.create(
		person_name = person[0],
		lives_in_town = person[1],
		nickname = person[2])
	new_person.save()

print('Reading and print all Persons...')
for person in Person:
	print(person.person_name, person.lives_in_town, person.nickname)


print('Read and print by selecting the name of one Person name...')

aperson = Person.get(Person.person_name == 'Susan')
print(aperson.nickname)


print('Read and print by looking for Person data items that are not missing')

for aperson in Person.select().where(Person.nickname != ''):
	print(aperson.person_name)

print('Update a missing nickname and check...')
aperson = Person.get(Person.person_name == 'Peter')
aperson.nickname = 'Painter'
aperson.save()

for aperson in Person.select().where(Person.nickname != ''):
	print(aperson.person_name)

print('Add and display a Person; then delete...')
new_person = Person.create(
	person_name = 'Fred',
	lives_in_town = 'Seattle',
	nickname = 'Fearless')
new_person.save()

aperson = Person.get(Person.person_name == 'Fred')
print(aperson.person_name, aperson.lives_in_town, aperson.nickname)
aperson.delete_instance()

print('Reading and print all Person (but not Fred)...')
for person in Person:
	print(person.person_name, person.lives_in_town, person.nickname)

print('JOBS')

print('Creating Jobs...')

jobs = [
	('Analyst', '2001-09-22', '2003-01-30',65500, 'Andrew'),
	('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew'),
	('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew'),	
	('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Peter'),
	('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Peter')

	]

for job in jobs:
	new_job = Job.create(
		job_name = job[0], 
		start_date = job[1],
		end_date = job[2],
		salary = job[3],
		person_employed = job[4]
		) 

	new_job.save()

print('Reading and print all Job...')

for job in Job:
	print(job.job_name, job.start_date, job.end_date, job.salary, job.person_employed)

print('Resolve the join and print...')

query = (Person
         .select(Person, Job)
         .join(Job, JOIN.LEFT_OUTER)
		)
for person in query:
    print(person.person_name, person.job.job_name)


print('Try to add a new job where a person doesnt exist...')

print('Try to Delete a person who has jobs...')

print('Try to change the name of a Person...')



database.close()