########
#modules
########
import csv
import sys
import collections
import datetime

########
#enter csv
########
path = "crime.csv"
datafile = open(path) #, newline=''
# reader function to parse csv data from file
reader = csv.reader(datafile)
#first line is header
header = next(reader)  #next function extracts first line
#now we read data 
data = [row for row in reader]

########

########
#functions
########
  

def date_to_day(date):
	date_format = date.split(' ')[0].split('-')
	day = int(date_format[0])
	month = int(date_format[1])
	year = int('20'+date_format[2])
	born = datetime.date(year, month, day)

	return born.strftime("%A")

def num_2015():
	num_crimes_2015 = 0
	for i in range(len(data)):
	
		#python find() returns -1 if not found
		if data[i][7].find("-15") != -1:
			num_crimes_2015 = num_crimes_2015 + 1

	print(num_crimes_2015)
	

def shootings_2018():
	num_shootings_2018=0

	for i in range(len(data)):
		if (data[i][6] != '') and (data[i][7].find("-18") != -1):
			num_shootings_2018 = num_shootings_2018 + 1

	print(num_shootings_2018)
	
def larceny_2017():
	num_larceny = 0

	for i in range(len(data)):
		if (data[i][2].find("Larceny") != -1) and (data[i][7].find("-17") != -1):
			num_larceny = num_larceny + 1

	print(num_larceny)

def drugviolation_AB():
	num_violations = 0

	for i in range(len(data)):
		if (data[i][4].find("A") != -1) or (data[i][4].find("B") != -1):
			if (data[i][2].find("Drug Violation") != -1):
				num_violations = num_violations + 1
	
	print(num_violations)

def common_codes():
	data.sort(reverse=True)
	new_list = []

	for i in range(len(data)):
		if data[i][7].find("-16") != -1:
	 		new_list.append(data[i][1])

	new_list.sort(reverse=True)

	c = collections.Counter(new_list)

	c = [key for key, _ in c.most_common(2)]
	
	print(c[0])
	return(c[1])
	
	
def most_robberies():
	#empty array to store collection of most
	array = []

	for b in ["-18", "-17", "-16", "-15", "-14"]:
		counter = 0
		for i in range(len(data)):
		 	if (data[i][2].find("Robbery") != -1) and (data[i][7].find(b) != -1):
		 		counter = counter + 1
		array.append([counter, b])

	array.sort(reverse=True)
	print('20'+array[0][1][1:] + '\n20'+ array[1][1][1:])


def crime_streets():
	data.sort(reverse=True)
	new_list = []

	for i in range(len(data)):
		if data[i][9].find(" ") != -1:
	 		new_list.append(data[i][9])

	new_list.sort(reverse=True)

	c = collections.Counter(new_list)

	c = [key for key, _ in c.most_common(3)]



	print(c[0])
	print(c[1])
	print(c[2])


def offense_codes():

	list2 = []

	districts = ["A","E","C"]

			
	
	for i in range(len(data)):
		if data[i][4].find(districts[0]) != -1:
			if date_to_day(str(data[i][7][0:8])) == "Friday" or date_to_day(str(data[i][7][0:8])) == "Saturday" or date_to_day(str(data[i][7][0:8])) == "Sunday":
				list2.append(data[i][1])
			

		if data[i][4].find(districts[1]) != -1:
			if date_to_day(str(data[i][7][0:8])) == "Friday" or date_to_day(str(data[i][7][0:8])) == "Saturday" or date_to_day(str(data[i][7][0:8])) == "Sunday":
				list2.append(data[i][1])

		if data[i][4].find(districts[2]) != -1:
			if date_to_day(str(data[i][7][0:8])) == "Friday" or date_to_day(str(data[i][7][0:8])) == "Saturday" or date_to_day(str(data[i][7][0:8])) == "Sunday":
				list2.append(data[i][1])

	list2.sort(reverse=True)

	#powerful function

	c  = collections.Counter(list2)

	c = [key for key, _ in c.most_common(3)]


	num1code = str(c[0])
	num2code = str(c[1])
	num3code = str(c[2])

	topcodes = [num1code,num2code,num3code]



## convert offense codes to offense code groups

	printarray1 = []
	printarray2 = []
	printarray3 = []

	for i in range(len(data)):
		if data[i][1] == topcodes[0]:
			printarray1.append(data[i][2])
		else:
			continue

	for i in range(len(data)):
		if data[i][1] == topcodes[1]:
			printarray2.append(data[i][2])
		else:
			continue
		
	for i in range(len(data)):
		if data[i][1] == topcodes[2]:
			printarray3.append(data[i][2])
			
		else:	
			continue


	print(printarray1[0])
	print(printarray2[0])
	print(printarray3[0])




########
#cases
#######

#condition 0 - student number
input = sys.argv[1]
if input == 'studentnumber':
	student_no = 3726450 
	print(student_no) 

#condition 1 - number of crimes in 2015
if input == '1': 
	num_2015()

#condition 2 - number of shootings in 2018
if input == '2':
	shootings_2018()

#condition 3 - number of larcony

if input == '3':
	larceny_2017()

#condition 4 - number of drug violations in district A and B
if input == '4':
	drugviolation_AB()
	

#condition 5 - most common codes in 2016
if input == '5':
	print(common_codes())


#condition 6 - two years with most robberies

if input == '6':
	most_robberies()


#condition 7 - top three non null streets in terms of incidents reported

if input == "7":
	crime_streets()

#condition 8 - 

if input == "8":
	offense_codes()
########
