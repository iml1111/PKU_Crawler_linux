from recent_date import get_today

def start_error_logging():
	try:
		f = open("/home/ubuntu/crawl_log.txt",'a')
	except:
		f = open("crawl_log.txt",'a')
	f.write("------" + get_today() + " Crawling Start.------\n")
	f.close()

def error_logging(page, info):
	try:
		f = open("/home/ubuntu/crawl_log.txt",'a')
	except:
		f = open("crawl_log.txt",'a')
	f.write(get_today() + " : [" + page + "] : " + info + "\n")
	print(get_today() + " : [" + page + "] : " + info + "\n")
	f.close()