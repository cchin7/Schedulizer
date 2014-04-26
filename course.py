class course(object):
#-------------------------------------------------------------------
    #Constructor
    def __init__(self, CRN, subj, courseNumber, title, location, credits, attributes, grades, days, time, isExist, isCompleted):
       self.__CRN = CRN
       self.__subj = subj
       self.__courseNumber = courseNumber
       self.__title = title
       self.__location = location
       self.__credits = credits
       self.__attributes = attributes
       self.__grades = grades
       self.__days = days
       self.__time = time
       self.__isExist = isExist
       self.__isCompleted = isCompleted
#-------------------------------------------------------------------
    #Accessors
    def getCRN(self):
        return self.__CRN
    def getSubj(self):
      	return self.__subj
    def getCourseNumber(self):
    	return self.__courseNumber
   	def getTitle(self):
   		return self.__title
   	def getLocation(self):
   		return self.__location
   	def getCredits(self):
   		return self.__credits
   	def getAttributes(self):
   		return self.__attributes
   	def getGrades(self):
   		return self.__grades
   	def getDays(self):
   		return self.__days
   	def getTime(self):
   		return self.__time
   	def getIsExist(self):
   		return self.__isExist
   	def getIsCompleted(self):
   		return self.__isCompleted
#-------------------------------------------------------------------
	#Mutator
	def setCRN(self,CRN):
		self.__CRN = CRN
    def setSubj(self,subj):
        self.__subj = subj
    def setCourseNumber(self,courseNumber):
        self.__courseNumber = courseNumber
   	def setTitle(self,title):
   		self.__title = title
   	def setLocation(self,location):
   		self.__location = location
   	def setCredits(self, credits):
   		self.__credits = credits
   	def setAttributes(self,attributes):
   		self.__attributes = attributes
   	def setGrades(self,grades):
   		self.__grades = grades
   	def setDays(self,days):
   		self.__days = days
   	def setTime(self,time):
   		self.__time = time
   	def setIsExist(self,isExist):
   		self.__isExist = isExist
   	def setIsCompleted(self,isCompleted):
   		self.__isCompleted = isCompleted

def validateCRN(CRN):
	result = CRN.isdigit()
	return result

def validateSubj(subj):
	result = subj.isalpha()
	return result

def validateCourseNumber(courseNumber):
	result = courseNumber.isdigit()
	return result

'''
def validateTitle(title):
	
	return result
'''

'''
def validateLocation(location):
	
	return result
'''

def validateCredit(credits):
	result = credits.isdigit()
	return result

def validateAttributes(attributes):
	result = attributes.isalpha()
	if result:
		attributeList = ["A","Y",""] #working
		if attributes.upper() in attributeList:
			result = True
		else:
			result = False
	return result

def validateGrades(grades):
	result = grades.isalpha()
	if result:
		gradesList = ["A","A-","B+","B","B-","C+","C","C-","D","F","P"]
		if grades.upper() in gradesList:
			result = True
		else:
			result = False
	return result

def validateDays(days):
	#Future Development: multiple days
	result = days.isalpha()
	if result:
		daysList = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
		if days.upper() in daysList:
			result = True
		else:
			result = False
	return result

'''
def validateTime(time):

	return result
'''

def main():
	