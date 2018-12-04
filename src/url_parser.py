from urllib.request import FancyURLopener, HTTPError
import time

class AppURLopener(FancyURLopener):     			 
   	version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
   	def http_error_default(self, url, fp, errcode, errmsg, headers):
   		if errcode == 403:
   			raise ValueError("403")
   		return super(AppURLopener, self).http_error_default(url, fp, errcode, errmsg, headers)

def URLparser(URL):
	try:
		html = AppURLopener().open(URL)
	except:
		time.sleep(1)
		print("Connection Error")
		try:
			html = AppURLopener().open(URL)
		except:
			return None
	return html
