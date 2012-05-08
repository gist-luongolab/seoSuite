import ConfigParser
import logging
import KeywordTrackingPositionException

class ExtractConfigurationFromCFGfiles:

	def __init__(self):
		self._options = {}
	
	def __dumpConfigurationFile(config):
		# dump entire config file
		for section in config.sections():
			parameters = []
			for option in config.options(section):
				parameters.add(config.get(section, option)
				#print " %s = %s" % (option,config.get(section, option))
			
			#self._get_options()[section] = parameters	

	@staticmethod
	def readFromCfgFile(filename="", section = "", attribute = ""):
		try:
			config = ConfigParser.RawConfigParser()
			if len(filename) > 0:
				config.read(filename)
			else:
				raise KeywordTrackingPositionException("Filename pass as argument!")
					
			self.__dumpConfigurationFile(config)

		except ConfigParser.NoSectionError:
			logging.error("Section does not exist!") 
		except KeywordTrackingPositionException as error:
			print error.value
