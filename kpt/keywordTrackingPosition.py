import re
from urlparse import urlparse
from xgoogle.search import GoogleSearch, SearchError


class KeywordTrackingPosition:


	def __makeUrl(self, domain):
		"""
    	convert domain into a nicer one (eg. www3.google.com into google.com)
    	
    	"""
		domain = re.sub("^www(\d+)?\.", "", domain)
		
		return domain



	def startSearch(self, domain = "",target_keywords = []):
		gs = GoogleSearch(target_keyword)
		gs.results_per_page = 100
		results = gs.get_results()
		for idx, res in enumerate(results):
			parsed = urlparse(res.url)
			domain = self.__makeUrl(parsed.netloc)
			if domain == target_domain:
				print "Ranking position %d for keyword %s on domain %s" % (idx+1, target_keyword, target_domain) 





