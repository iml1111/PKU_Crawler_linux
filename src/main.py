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
from db_manager import db_manage
from recent_date import get_today
from elog import start_error_logging

#for Debug
target = "PK_univ"
URL = List[31:32] 


if __name__ == '__main__':
	print("HI! I'M IML.")
	print('First Crawling Start!')
	print('target: ' + target)

	start_error_logging()

	for url in URL:
		print('< URL parsing Start! >\n' + str(url['url']))
		Crawling(target, url, True)
		print('-------------------------------------')

	PK_etc.crawling()


			
			
		
