from url_parser import URLparser
from bs4 import BeautifulSoup
from db_manager import db_manage
from PK_global import startdate_dict
from tag import tagging
from recent_date import get_recent_date

def parsing(driver, URL, is_first):
	if is_first == False:
		latest_datetime = db_manage("get_recent", URL['info'])
	recent_date = None
	page = 1
	while True:
		print('this page is\t| '+ URL['info'] + ' |\t' + str(page))
		bs0bj = BeautifulSoup(driver.read(), "html.parser")
		bs0bj = bs0bj.find("td",{"class":"text12graylight"}).find('td',{"valign":"top"}).find("table")
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
			driver = URLparser(URL['url'] + "&page=" + str(page))
			print(URL['url'] + "&page=" + str(page - 1))

	# 최근 날짜가 갱신되었다면 db에도 갱신
	if recent_date != None:
		db_manage("renewal_date", URL['info'], recent_date, is_first = is_first)
	recent_date = None


def list_parse(bs0bj, URL, page, latest_datetime = None):
	target = URL['info'].split('_')[1]
	start_datetime = startdate_dict[target]
	db_docs = []
	post_list = bs0bj.findAll("td",{"height":"29"})
	domain = URL['url'].split('/')[0] + '//' + URL['url'].split('/')[2] + '/'\
	 + URL['url'].split('/')[3] + '/' + URL['url'].split('/')[4] + '/'

	for post in post_list:
		db_record = {}

		obj = post.find("a",{"class":"text12graylightlink"})
		db_record.update({"url": domain+ obj.attrs['href']})
		db_record.update({"title":obj.get_text().strip()})

		obj = post.find("td",{"width":"70"}).get_text().strip()
		obj = obj.replace(".","-")
		db_record.update({"date":obj})
		db_record.update({"post":0})
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