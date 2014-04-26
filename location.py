class location(object):
	"""
	location class
	Attributes:
	building - letters
	roomNumber - digits

	print strings
	"""
#-------------------------------------------------------------------
	#Constructor
	def __init__(self,building,roomNumber):
		self.__building = building
		self.__roomNumber = roomNumber
#-------------------------------------------------------------------
	#Accessor
	def getBuilding(self):
		return self.__building

	def getRoomNumber(self):
		return self.__roomNumber

	def __str__(self):
		return self.__building + " " + str(self.__roomNumber)
#-------------------------------------------------------------------
	#Mutator
	def setBuilding(self,building):
		self.__building = building

	def setRoomNumber(self,roomNumber):
		self.__roomNumber = roomNumber