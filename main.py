'''
kernel for schedulizer

needs:
	course.py
	validateInput.py
	location.py

form a list of course objects
'''

from course import *
from validateInput import *
from location import *

i = 1
courseDict = {}
while True:
	print("---course #" + str(i) + "---")

	while True:
		CRN = input("CRN: ")
		if validateCRN(CRN):
			CRN = int(CRN)
			break
		else:
			print("WARNING: CRN is in digits")

	while True:
		subj = input("Subject: ")
		if validateSubj(subj):
			subj = subj.upper()
			break
		else:
			print("WARNING: Subject is in letters")

	while True:
		courseNumber = input("Course Number: ")
		if validateCourseNumber(courseNumber):
			courseNumber = int(courseNumber)
			break
		else:
			print("WARNING: Course Number is in digits")

	while True:
		title = input("Course Title: ")
		if validateTitle(title):
			break
		else:
			print("WARNING: Title is a string")

	while True:
		building = input("Building: ")
		if validateBuilding(building):
			building = building.upper()
			break
		else:
			print("WARNING: Building is in letters")

	while True:
		roomNumber = input("Room Number: ")
		if validateRoomNumber(roomNumber):
			if not roomNumber.isdigit():
				roomNumber = roomNumber[0].upper() + roomNumber[1:]
			break
		else:
			print("WARNING: e.g. G### or ###")

	while True:
		credits = input ("Credits: ")
		if validateCredits(credits):
			credits = int(credits)
			break
		else:
			print("WARNING: Credits is in digits")

	while True:
		attributes = []
		while True:
			char = input("Attributes: ").upper()
			if validateAttributes(char):
				break
			else:
				print('WARNING: Attributes Options:'+ str(attributesTuple))
		attributes.append(char)
		if not attributes[0] == "NA":
			while True:
				answer = input ("More Attributes? Y/N: ").upper()
				if answer in ("Y","N"):
					break
			if answer == "N":
				break
		else:
			break

	while True:
		grades = input ("Grades: ")
		grades = grades[0].upper() + grades[1:]
		if validateGrades(grades):
			break
		else:
			print('WARNING: Grades Options:' + str(gradesTuple))
	
	while True:
		days = []
		while True:
			char = input ("Days: ")
			if validateDays(char):
				break
			else:
				print('WARNING: Days Options:'+str(daysTuple))
		days.append(char)
		while True:
			answer = input ("More days? Y/N: ").upper()
			if answer in ("Y","N"):
				break
		if answer == "N":
			break

	while True:
		isExist = input("Exist? T/F: ").upper()
		if isExist in ("T","F"):
			break
	isExist = {"T":True,"F":False}[isExist]

	while True:
		isCompleted = input("Completed? T/F: ").upper()
		if isCompleted in ("T","F"):
			break
	isCompleted = {"T":True,"F":False}[isCompleted]

	locationObj = location(building,roomNumber)
	courseObj = course(CRN, subj, courseNumber, title, locationObj, credits, attributes, grades, days, isExist, isCompleted)
	courseDict[courseObj.getCRN()] = courseObj
	print(courseDict[courseObj.getCRN()])

	del courseObj
	del locationObj

	while True:
		answer = input("Add more courses? T/F: ").upper()
		if answer in ("T","F"):
			break
	if not {"T":True,"F":False}[answer]:
		print(str(i) + " course(s) added.")
		break
	i += 1

print (courseDict)