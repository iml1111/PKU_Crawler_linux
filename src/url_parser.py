import requests
import time

header = {
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
			"Accept":"text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8"}

def URLparser(URL):
	
	try:
		html = requests.get(URL, verify = False, headers = header).text
	except:
		time.sleep(3)
		print("Connection Error")
		try:
			html = requests.get(URL, verify = False,  headers = header).text
		except:
			return None
	return html

def URLparser_con(URL, enc):
	try:
		html = requests.get(URL, verify = False,  headers = header).content.decode(enc)
	except:
		time.sleep(3)
		print("Connection Error")
		try:
			html = requests.get(URL, verify = False,  headers = header).content.decode(enc)
		except:
			return None
	return html	
