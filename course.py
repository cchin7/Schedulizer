class course(object):
  '''
  (CRN, subj, courseNumber, title, location, credits, attributes, grades, days, isExist, isCompleted)
  CRN: numbers
  subj: letters
  courseNumber: all numbers
  title: course title
  location: location object
  credits: numbers
  attributes: LIST of letters that belongs to attributesList in validateInput.py
  grades: a letter that belongs to gradesList in validateInput.py
  days: LIST that belongs to daysList in validateInput.py
  isExist: Boolean value (T if course has been added to the schedule)
  isCompleted: Boolean Value (T if course has been completed)
  '''
#-------------------------------------------------------------------
  #Constructor
  def __init__(self, CRN, subj, courseNumber, title, location, credits, attributes, grades, days, isExist, isCompleted):
    self.__CRN = CRN
    self.__subj = subj
    self.__courseNumber = courseNumber
    self.__title = title
    self.__location = location
    self.__credits = credits
    self.__attributes = attributes
    self.__grades = grades
    self.__days = days
#    self.__time = time
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
#  def getTime(self):
#    return self.__time
  def getIsExist(self):
    return self.__isExist
  def getIsCompleted(self):
    return self.__isCompleted
  def __str__(self):
    return '\n' + self.__subj + " " + str(self.__courseNumber) + "\t" + self.__title + '\n' + "Days: " +'\t\t' + str(self.__days) + '\n' + "Location:" + '\t' + str(self.__location) + '\n' + "Credits: " + '\t' + str(self.__credits) + '\n' + "Attributes: " + '\t' + str(self.__attributes) + '\n' + "Grades: " + '\t' + self.__grades + '\n' + "isExist: " + '\t' + str(self.__isExist) + '\n' + 'isCompleted:' + '\t' + str(self.__isCompleted) + '\n'

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
#  def setTime(self,time):
#    self.__time = time
  def setIsExist(self,isExist):
    self.__isExist = isExist
  def setIsCompleted(self,isCompleted):
    self.__isCompleted = isCompleted