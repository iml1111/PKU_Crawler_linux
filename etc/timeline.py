import pymongo 
import random
import datetime

now = datetime.datetime.now() - datetime.timedelta(days = 90)
date = now.strftime("%Y-%m-%d %H:%M:%S")

db_name = 'pookle'
ip = 'localhost'
port = 27017

def View(db, itag, etag):
	from operator import itemgetter
	from random import shuffle
	result = []
	degree_list = []

	if "공지" in itag:
		is_main = True
	else:
		is_main = False

	for i in itag:
		if i.endswith("학과") == True or i.endswith("교육과") == True \
			or i.endswith("학부") == True:
			degree_list.append(i)

	for col in db.collection_names():
		if col.startswith("PK_") == False:
				continue
		#메인타임라인의 경우 타학과공지 제외
		if is_main == True:
			coll_list = list(db[col].find(
														{"$and":[
																{"tag":{ "$in": itag }},	
																{"$or":[
																	{"$and":[
																			{"tag": {"$not": {"$elemMatch":{"$regex":"학과$"}}}},
																			{"tag":{"$not": {"$elemMatch":{"$regex":"학부$"}}}},
																			{"tag":{"$not": {"$elemMatch":{"$regex":"교육과$"}}}}
																		]
																	},
																	{"tag": {"$in": degree_list}},
																	]
																},
																{"tag":{"$nin":etag }}
															]
														}))
		#서브타임라인의 경우 타학과 게시글 포함
		else: 
			coll_list = list(db[col].find(
														{"$and":[
																{"tag":{ "$in": itag }},	
																{"tag":{"$nin":etag }}
															]
														}))
		#3달이내의 글만 갖고옴
		for i in coll_list:
			if i['date'] >= date:
				result.append(i)

	#fav_list = sorted(result, key=itemgetter("fav_cnt","view","date"), reverse = True)
	fav_list = sorted(result, key=itemgetter("date"), reverse = True)
	#if fav_list[0]['fav_cnt'] == 0 and fav_list[0]['view'] == 0:
	#	shuffle(fav_list)
	for q in range(5): shuffle(result)
	normal_list = result
	

	fav_line = 0
	normal_line = 0
	result = []

	if len(fav_list) >= 300:
		rng = 300
	else:
		rng = len(fav_list)
	for i in range(rng):

		if (i % 3 == 0  or normal_line >= len(normal_list)) and  fav_line < len(fav_list):
			post = fav_list[fav_line]
			fav_line += 1
		elif (i % 3 != 0 or fav_line >= len(fav_list))  and normal_line < len(normal_list): 
			post = normal_list[normal_line]
			normal_line += 1
		
		is_dedup = False
		for j in result:
			if post['_id'] == j['_id']:
				is_dedup = True
				break
		if is_dedup == True:
			continue
		else:
			result.append(post)
	return result

def db_access():
	client = pymongo.MongoClient(ip,port)
	db = client[db_name]
	return db

if __name__ == '__main__':

	include_tag = [
	#메인
	["기타","공지","거래","대나무숲","반짝정원","지식인","장학"],
	#진로
	["창업지원단","취업","창업","진로"],
	#스터디&모임
	['스터디&모임',"특강","세미나","봉사","동아리"],
	#알바&구인
	["조교","과외&강사","알바&구인"],
	#행사&대외활동
	["행사","봉사","공모전&대외활동","교육&설명회","멘토링"],
	]
	exclude_tag = []
	
	List =View(db_access(),include_tag[0], exclude_tag)
	for i in range(10):
		print(List[i]['title'])
		print(List[i]['tag'])
		print(List[i]['date'])
		print()
	print(len(List))
