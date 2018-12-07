"""	      U&I_Crawler		"""
"""	     	BY IML  		"""
"""	shin10256|gmail.com   	"""	
"""	shino1025.blog.me    	"""
"""	github.com/iml1111   	"""
import iml_global
from url_list import List
from crawl_select import Crawling
import PK_etc
import time
from recent_date import get_today

#for Debug
target = "PK_univ"
URL = List[91:] 


if __name__ == '__main__':
	print("HI! I'M IML.")
	print('First Crawling Start!')
	print('target: ' + target)

	mode = input("mode Select: ")
	
# Start mode
	if mode == "1":

		for url in URL:
			print('< URL parsing Start! >\n' + str(url['url']))
			Crawling(target, url, True)
			print('-------------------------------------')

		PK_etc.crawling()

# Renewal mode
	else:
		while(True):
			print('\n\nRenewal Crawling Start...\n\n')
			for url in URL:
				print('< URL parsing Renewal >\n' + str(url['url']))
				Crawling(target, url, False)
				print('-------------------------------------')
			print("waiting....")
			print(get_today())
			time.sleep(60*60)
			
			
		
