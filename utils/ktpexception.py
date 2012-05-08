
class KeywordTrackingPositionException(Exception):
	def __init__(self, value=""):
		self.__value = value

	def __str__(self):
		return "(Exception) - %s" % (self.__value)

