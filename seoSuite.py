import sys
from utils.ecf import ExtractConfigurationFromCFGfiles
from ktp.KeywordTrackingPosition import KeywordTrackingPosition

if __name__ == '__main__':
	ecff = ExtractConfigurationFromCFGfiles()
	ecff.readFromCfgFile(sys.argv[1:])
	options = ecff._get_options()
	print options
	#ktposition = KeywordTrackingPosition()
