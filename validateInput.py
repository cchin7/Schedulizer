'''
validate Inputs for course.py

return True if all inputs are valid, return False otherwise

validateAll: take a list in the form of (CRN, subj, courseNumber, title, building, roomNumber, credits, attributes, grades, days, isExist, isCompleted)

location has to be a location object
attributesTuple = ["A","Y","P","N","B","M","C","O","J","G","H","S","L","NA"]
gradesTuple = ["A","A-","B+","B","B-","C+","C","C-","D","F","P","I"]
daysTuple = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
'''
attributesTuple = ("A","Y","P","N","B","M","C","O","J","G","H","S","L","NA")
gradesTuple = ("A","A-","B+","B","B-","C+","C","C-","D","F","P","I")
daysTuple = ("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY")


def validateCRN(CRN):
	return str(CRN).isdigit()

def validateSubj(subj):
	return subj.isalpha()

def validateCourseNumber(courseNumber):
	return str(courseNumber).isdigit()

def validateTitle(title):
	return isinstance(title,str)

def validateBuilding(building):
	return building.isalpha()

def validateRoomNumber(roomNumber):
	if roomNumber.isdigit():
		return True
	elif roomNumber[1:].isdigit():
		if roomNumber[0].isalpha():
			return True
		else:
			return False
	else:
		return False

def validateLocation(location):
	if not isinstance(location,location):
		return False
	if not location.getBuilding().isalpha():
		return False
	if not str(location.getRoomNumber()).isdigit():
		return False
	return True

def validateCredits(credits):
	return str(credits).isdigit()

def validateAttributes(attributes):
	return attributes.upper() in attributesTuple

def validateAllAttributes(attributes):
	if not isinstance(attributes,list):
		return False
	for char in attributes:
		if not char.isalpha():
			return False
		if not char.upper() in attributesTuple:
			return False
	return True

def validateGrades(grades):
	grades = grades[0].upper() + grades[1:]
	return grades in gradesTuple

def validateAllGrades(grades):
	if not isinstance(grades,str):
		return False
	if not grades.isalpha():
		return False
	if grades.upper() in gradesTuple:
		return True
	else:
		return False

def validateDays(days):
	return days.upper() in daysTuple

def validateAllDays(days):
	#Future Development: multiple days
	if not isinstance(days,list):
		return False
	for char in days:
		if not char.isalpha():
			return False
		if not char.upper() in daysTuple:
			return False
	return True

'''
def validateTime(time):
	#needs work
	return True
'''

def validateIsExist(isExist):
	return isinstance(isExist,bool)

def validateIsCompleted(isCompleted):
	return isinstance(isCompleted,bool)

'''
def validateAll(inputList):
	inputTuple = tuple(inputList)

	if validateCRN(inputTuple[0]):
		print ("CRN \t\t OK")
	else:
		return False

	if validateSubj(inputTuple[1]):
		print ("Subj \t\t OK")
	else:
		return False

	if validateCourseNumber(inputTuple[2]):
		print ("courseNumber \t OK")
	else:
		return False

	if validateTitle(inputTuple[3]):
		print ("title \t\t OK")
	else:
		return False

	if validateBuilding(inputTuple[4]):
		print ("Building \t\t OK")
	else:
		return False

	if validateRoomNumber(inputTuple[5]):
		print ("Room Number \t\t OK")
	else:
		return False

	if validateCredits(inputTuple[6]):
		print ("credits \t\t OK")
	else:
		return False

	if validateAttributes(inputTuple[7]):
		print ("Attributes \t\t OK")
	else:
		return False

	if validateGrades(inputTuple[8]):
		print ("grades \t\t OK")
	else:
		return False

	if validateDays(inputTuple[9]):
		print ("days \t\t OK")
	else:
		return False

	if validateIsExist(inputTuple[10]):
		print ("isExist \t\t OK")
	else:
		return False

	if validateIsCompleted(inputTuple[11]):
		print ("isCompleted \t\t OK")
	else:
		return False

	return True
'''