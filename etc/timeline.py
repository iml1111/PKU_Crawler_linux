import pymongo 
import datetime
from operator import itemgetter
from random import shuffle, randrange

now = datetime.datetime.now() - datetime.timedelta(days = 10)
date = now.strftime("%Y-%m-%d %H:%M:%S")
now2 = datetime.datetime.now() - datetime.timedelta(days = 20)
date2 = now2.strftime("%Y-%m-%d %H:%M:%S")

fav_cut = 15
view_cut = 50

include_coll =["PK_main_notice","PK_main_free","PK_main_openmarket",
	"PK_main_boarding","PK_main_lost","PK_main_car","PK_pknu_bamboo",
	"PK_pknu_public","PK_pknu_lost","PK_pknu_free","PK_pknu_twinkle",
	"PK_pknu_kin","PK_today_today","PK_pknulogin_market",
	"PK_dorm_notice","PK_dcinside_free", "PK_sh_notice","PK_start_notice"]
include_tag = ["기타","공지","거래","대나무숲","반짝정원","지식인","장학"]
priority_tag = []
	#"컴퓨터공학과","취업","영어","대나무숲"
exclude_tag = []

db_name = 'pookle'
ip = 'localhost'
port = 27017

def db_access():
	client = pymongo.MongoClient(ip,port)
	db = client[db_name]
	return db

def View(db, icoll, itag, ltag, etag):
	
	result = []
	tag = list(set(itag + ltag))
	for col in db.collection_names():
		# 메인타임라인의 기본 콜렉션
		if any(icol in col for icol in icoll):
			coll_list = list(db[col].find(
														{"$and":[
																{"date":{"$gt":date}},
																{"tag":{ "$in": tag }},	
																{"tag":{"$nin":etag }},
																
															]
														}))
		#기본 콜렉션 외의 로그인 태그 게시글 여부
		else:
			coll_list = list(db[col].find(
														{"$and":[
																{"date":{"$gt":date2}},
																{"tag":{ "$in":ltag }},	
																{"tag":{"$nin":etag }},				
															]
														}))
		result += coll_list

	for post in result:
		if any(tag in ltag for tag in post['tag']):
			post.update({"priority":True})
		else:
			post.update({"priority":False})

		if post['fav_cnt'] < fav_cut:
			post.update({"fav_cnt2":0})
		else:
			post.update({"fav_cnt2":post['fav_cnt']})

		if post['view'] < view_cut:
			post.update({"view2":0})
		else:
			post.update({"view2":post['view']})

	fav_list = sorted(result, key=itemgetter("priority","fav_cnt2","view2","date"), reverse = True)
	result = sorted(result, key=itemgetter("date"), reverse = True)
	fav_cnt = 0

	for i in range(len(result)):
		if i >= 240 or fav_cnt >= 80 or i >= len(result):
			break
		if randrange(100) <= 50 \
		and any(fav_list[fav_cnt] == j["_id"] for j in result[0:i]) == False:
			result.insert(i, fav_list[fav_cnt])
			fav_cnt += 1

	i = 0
	while(True):
		if i >= len(result):
			break
		for j in range(i + 1, len(result)):
			if result[i]['_id'] == result[j]['_id']:
				del result[j]
				break
		i += 1
	#디시 제거 
	'''
	for i in range(len(result)-4):
		if i >= len(result)-4:
			break
		while(i < len(result)-3 and "디시인사이드" in result[i]['tag'] and\
		"디시인사이드" in result[i + 1]['tag']):
			delete_list = sorted(result[i:i+2],key=itemgetter("fav_cnt","view","date"))
			if delete_list[0]['title'] == result[i]['title']:
				del result[i]
			elif delete_list[0]['title'] == result[i+1]['title']:
				del result[i+1]
	'''
	
	#광고사이에 껴넣기
	index = 10
	ad_list = list(db['advertise'].find())
	shuffle(ad_list)
	for ad in ad_list:
		result.insert(index, ad)
		index += 11

	return result


if __name__ == '__main__':
	import time

	start_time = time.time()
	db = db_access()
	List =View(db, include_coll, include_tag, priority_tag, exclude_tag)
	end_time = time.time() - start_time

	for i in range(20):
		try:
			print(List[i]['title'])
			print(List[i]['tag'])
			print(List[i]['date'])
			print()
		except:
			pass
	print("총 게시글 수:",len(List))
	print("소요시간:",end_time)