from url_parser import URLparser
from bs4 import BeautifulSoup
from db_manager import db_manage
from PK_global import startdate_dict
from tag import tagging
from recent_date import get_recent_date
from post_wash import post_wash

start_datetime = None

def parsing(driver, URL, is_first):

	target = URL['info'].split('_')[1]
	global start_datetime
	start_datetime = startdate_dict[target]

	if is_first == False:
		latest_datetime = db_manage("get_recent", URL['info'])
	recent_date = None
	page = 1
	print("start_date:" + start_datetime)
	while True:
		print('this page is\t| '+ URL['info'] + ' |\t' + str(page))
		bs0bj = BeautifulSoup(driver.read(), "html.parser")
		bs0bj = bs0bj.find("div",{"id":"board_box"}).find("ul",{"id":"board_list"})

		# first 크롤링일 경우 그냥 진행
		if is_first == True:
			db_docs = list_parse(bs0bj, URL, page)

		# renewal 모드일 경우. DB에서 가장 최신 게시물의 정보를 가져옴.
		else:
			db_docs = list_parse(bs0bj, URL, page, latest_datetime)
		# 맨 첫 번째 페이지를 파싱했고, 해당 페이지에서 글을 가져온 경우
		# 해당 글을 최신 날짜를 딕셔너리로 저장
		if page == 1 and len(db_docs) >= 1:
			recent_date = get_recent_date(URL, db_docs)

		if len(db_docs) == 0:
			print("addOK : 0")
			break
		else:
			addok = db_manage("add", URL['info'], db_docs)
			print("addOK : " + str(addok))
			if addok == 0:
				break
			page += 1
			driver = URLparser(URL['url'] + "&pageIndex=" + str(page))

	# 최근 날짜가 갱신되었다면 db에도 갱신
	if recent_date != None:
		db_manage("renewal_date", URL['info'], recent_date, is_first = is_first)
	recent_date = None


def list_parse(bs0bj, URL, page, latest_datetime = None):
	db_docs = []
	post_list = bs0bj.findAll("li")
	domain = URL['url'].split('/')[0] + '//' + URL['url'].split('/')[2]

	for post in  post_list:
		db_record = {}
		try:
			obj = post.find("a").attrs['href']
		except Exception as e:
			return db_docs
		
		db_record.update(content_parse(domain + obj))
		db_record.update(tagging(URL, db_record['title']))

		print(db_record['date'])
		# first 파싱이고 해당 글의 시간 조건이 맞을 때
		if db_record['date'] >= start_datetime  and \
				latest_datetime == None:
			db_docs.append(db_record)
		#renewal 파싱이고 해당 글의 갱신 조건이 맞을 때
		elif latest_datetime != None and \
				db_record['date'] >= latest_datetime['recent_date'] and \
					db_record['title'] != latest_datetime['title']:
			db_docs.append(db_record)		
		else:
			continue

	return db_docs

def content_parse(url):
	db_record = {}
	html = URLparser(url)
	bs0bj = BeautifulSoup(html.read(), "html.parser")
	bs0bj = bs0bj.find("div",{"id":"board_view"})
	db_record.update({"url":url})

	obj = bs0bj.find("h3").get_text().strip()
	db_record.update({"title":obj})

	obj = bs0bj.find("p",{"class":"writer"}).find("strong").get_text().strip()
	db_record.update({"date":obj})

	try:
		obj = bs0bj.find("div",{"class":"board_stance"}).get_text().strip()
		db_record.update({"post":post_wash(obj)})
	except:
		db_record.update({"post":1})

	return db_record