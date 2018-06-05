'''
Lesson07 - Assignment1 
Implementation of the Mailroom functionalities using DB as backend
- 1 - Send a Thank You
- 2 - Create a Report
- 3 - Send letters to everyone
- 4 - Quit

Implemented Exception Handling for User Input - Entering donation amount and entering menu selection
Re-factored methods in the mailroom to enable being called from test cases
'''

#!/usr/bin/env python3

import logging
from peewee import *
from mailroom_db_model import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only


''' ************* Database Helper Functions to communicate with Backend DB**********'''
def add_donation(donor_name, donation_amt):	
	'''
	adds a donation record to the DB table
	'''
	with database.transaction():
		new_donation = Donation.create(donated_by = donor_name, donation_amount = donation_amt)
		new_donation.save()

def add_donor(donor_name):
	'''
	adds a donor to the DB table
	'''
	new_donor = Donor.create(donor_name = donor_name, donor_lives_in = '')
	new_donor.save()


def add_donor_without_amount(donor_full_name):
	'''
	adds a donor to the DB without any donation values
	'''
	if not does_donor_exist(donor_full_name):
		add_donor(donor_full_name)
		return True
	else:
		return False


def add_donation_to_existing_donor(donor_full_name, donation_amt):
	'''
	adds a donation amount to and existing donor in the DB
	'''
	if does_donor_exist(donor_full_name):
		try:
			add_donation (donor_full_name, float(donation_amt))
			return True
		except ValueError as e:
			print ("Exception occured in User Input for Menu: {}".format(e))
			print ("Invalid Format for Donation Amount. Enter a valid integer or Floating point number")
	return False

def does_donor_exist(donor_name):
	'''
	Checks if the donor exists in the DB
	'''
	query = (Donor.select(donor_name).where (Donor.donor_name == donor_name))
	if (query.dicts().count() > 0):
		return True
	else: return False

def get_donor_names():
	'''
	returns the list of donors in the DB as a list
	'''
	donors = []
	for donor_row in Donor:
		donors.append(donor_row.donor_name)
	return donors

def get_donor_count():
	'''
	returns the count of Donors in the DB
	'''
	query = Donor.select(Donor.donor_name)
	return query.dicts().count()


def get_donation_amounts_list_for_donor(donor_name):
	'''
	gets the donation amounts list for a donor
	'''
	donations = []
	query = (Donation.select(Donation.donation_amount).where (Donation.donated_by == donor_name))
 
	for tmp_row in query.dicts():
		val = tmp_row['donation_amount'] #DB returns val in format : {'donation_amount': Decimal('129000.95')}
		donations.append(float(val))

	return donations


'''*********** MAILROOM FUNCTIONALITY ************'''


def send_letters_to_everyone():
	'''
	Generates letters to all the donors in the Donor list with DonorName.txt 
	Writes the files to the hard disk 
	'''
	donors_list = get_donor_names()
	for donor in donors_list:
		donations_list_for_donor = get_donation_amounts_list_for_donor(donor)
		total = 0 
		for item in donations_list_for_donor:
			total  = total + item
		letter = generate_letter(donor,donations_list_for_donor)
		filename = donor + ".txt"
		file = open(filename,"w")
		file.write(letter)
		file.close()
		print ("Generated letter with file name {} for Donor {}".format(filename,donor))

def generate_letter(donor, donations_list=None):
	'''
	Helper function to generate the letter in the specified format
	'''
	if donations_list == None: 
		donations_list = get_donation_amounts_list_for_donor(donor)
	amount = donations_list[-1] #most recent donation
	lettercontent = f"Dear {donor}, \n \t Thank You for your very kind donation of ${amount}. It will be put to very good use. \n \t \t Sincerely, \n \t \t \t The Team"
	return (lettercontent)


def send_thankyou():
	'''
	Function which implements the send Thank You functionality
	Use a while True loop 
		- condition to break from the while loop is once the Thank you note is printed
		- take user input for the name of the Donor
		- If the donor doesn't exist, add the donor info to the global dictionary
		- Use the donor and ask user to enter Donation amount and add it to the donation amounts in the Dictioary
		- If the user enters "list" , display all the donors 
	'''
	while True:		
		response_donor = input("Enter the Full Name of the Donor > ")
		donors = get_donor_names()

		if response_donor == "list":
			print ("List of Donors:")
			print (("{:30} "*len(donors)).format(*donors))
			continue 
		if response_donor not in donors:
			add_donor_without_amount(response_donor)
			#Add the new donor to the Donors List
		
		while True:
			try:
				response_amount = input("Enter the Amount of donation > ")
				add_donation_to_existing_donor(response_donor,float(response_amount))
				break #Break from while for Donation Amount Entry
			except ValueError as e:
				print ("Exception occured in User Input for Menu: {}".format(e))
				print ("Invalid Format for Donation Amount. Enter a valid integer or Floating point number")

		letter_content = generate_letter(response_donor)
		print (letter_content)
		return letter_content #Break and return from while loop for Donor Name Entry and the method


def create_report():
	'''
	Create a report in the format specified in the requirements - as shown below
	Donor Name                | Total Given | Num Gifts | Average Gift
	------------------------------------------------------------------
	William Gates, III         $  653784.49           2  $   326892.24
	Mark Zuckerberg            $   16396.10           3  $     5465.37
	Jeff Bezos                 $     877.33           1  $      877.33
	Paul Allen                 $     708.42           3  $      236.14

	Compute the Donor info along with total donation amount, number of gifts and average amount
		- store the info as tuples in a list - donorInfoList
	Print the Data in the specified format
	'''
	donorinfolist = []
	donors = get_donor_names()
	for donor in donors:
		total = 0 
		numgifts = 0
		for item in get_donation_amounts_list_for_donor(donor):
			total  = total + item
			numgifts = numgifts + 1
		avgamount = total/numgifts
		donorinfolist.append ((donor,total,numgifts,avgamount))
	sp1 = " " * 19
	header = "Donor Name " + sp1 + " | Total Given  | Num Gifts | Average Gift"
	print (header)
	dash = "-" * len(header)
	print (dash)
	for tmpitem in donorinfolist:
		print(f"{tmpitem[0]:30}  ${tmpitem[1]:10.2f}  {tmpitem[2]:10}    ${tmpitem[3]:10.2f}")



def exit():
	'''
	Method that ends the program
	'''
	print ("Exiting the program based on User Selection")
	quit()


'''
Global dictionary that stores the menu - key as the option number entered by user
value - is the corresponding method name that needs to be invoked for that menu
'''
dict_menu = {"1": send_thankyou,
			 "2" : create_report,
			 "3" : send_letters_to_everyone,
			 "4" : exit }


def main_menu():
	'''
	Function to display the Main Menu
	Takes input from user and the response is not valid - prompts the user to enter a valid response
	Returns the response from the user to the calling function
	'''
	print ("********** MAIN MENU **********")	
	print ("1 - Send a Thank You")
	print ("2 - Create a Report")
	print ("3 - Sent letters to everyone")
	print ("4 - Quit")
	while True:		
		response = input ("Enter 1 or 2 or 3 or 4 to select a Menu item > ")
		return response


'''Main Method'''
if __name__ == "__main__":
	#When the user selects Option 4, the program will Quit
	while True:
		try:
			dict_menu[main_menu()]()
		except KeyError as e:
			print ("Exception occured in User Input for Menu: {}".format(e))
			print ("Enter non empty and valid response - 1 or 2 or 3 or 4")
	
	database.close()

	


