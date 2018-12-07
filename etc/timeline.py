import pymongo 
import random
import datetime
import time

now = datetime.datetime.now() - datetime.timedelta(days = 30)
date = now.strftime("%Y-%m-%d %H:%M:%S")

db_name = 'pookle'
ip = 'localhost'
port = 27017

def db_access():
	client = pymongo.MongoClient(ip,port)
	db = client[db_name]
	return db

def View(db, icoll, itag, ltag, etag):
	from operator import itemgetter
	from random import shuffle
	result = []

	for col in db.collection_names():
		# 메인타임라인의 기본 콜렉션
		if any(icol in col for icol in icoll):
			coll_list = list(db[col].find(
														{"$and":[
																{"tag":{ "$in": itag + ltag }},	
																{"tag":{"$nin":etag }},
																{"date":{"$gt":date}}
															]
														}))
		#기본 콜렉션 외의 로그인 태그 게시글 여부
		else:
			coll_list = list(db[col].find(
														{"$and":[
																{"tag":{ "$in":ltag }},	
																{"tag":{"$nin":etag }},
																{"date":{"$gt":date}}
															]
														}))
		result += coll_list
	for post in result:
		if any(tag in ltag for tag in post['tag']):
			post.update({"priority":True})
		else:
			post.update({"priority":False})

	fav_list = sorted(result, key=itemgetter("priority","fav_cnt","view","date"), reverse = True)
	shuffle(result)
	fav_cnt = 0

	for i in range(len(result)):
		if i >= 240 or fav_cnt >= 80:
			break
		if random.randrange(100) <= 40 \
		and any(fav_list[fav_cnt] == j["_id"] for j in result[0:i]) == False:
			result.insert(i, fav_list[fav_cnt])
			fav_cnt += 1
		
	return result


if __name__ == '__main__':

	include_coll =["PK_main_notice","PK_main_free","PK_main_openmarket",
	"PK_main_boarding","PK_main_lost","PK_main_car","PK_pknu_bamboo",
	"PK_pknu_public","PK_pknu_lost","PK_pknu_free","PK_pknu_twinkle",
	"PK_pknu_kin","PK_today_today","PK_pknulogin_market",
	"PK_dorm_notice","PK_dcinside_free", "PK_sh_notice","PK_start_notice"]
	include_tag = ["기타","공지","거래","대나무숲","반짝정원","지식인","장학"]
	login_tag = ["컴퓨터공학과","영어"]
	exclude_tag = []
	

	start_time = time.time()
	db = db_access()
	List =View(db, include_coll, include_tag, login_tag, exclude_tag)
	end_time = time.time() - start_time

	for i in range(10):
		print(List[i]['title'])
		print(List[i]['tag'])
		print(List[i]['date'])
		print(List[i]['fav_cnt'])
	print(len(List))
	print(end_time)