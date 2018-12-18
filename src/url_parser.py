import requests
import time

def URLparser(URL):
	try:
		html = requests.get(URL, verify = False).text
	except:
		time.sleep(3)
		print("Connection Error")
		try:
			html = requests.get(URL, verify = False).text
		except:
			return None
	return html

def URLparser_con(URL, enc):
	try:
		html = requests.get(URL, verify = False).content.decode(enc)
	except:
		time.sleep(3)
		print("Connection Error")
		try:
			html = requests.get(URL, verify = False).content.decode(enc)
		except:
			return None
	return html	
