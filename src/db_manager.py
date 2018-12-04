import pymongo 
import os
import datetime
# 디버깅을 위한 코드, 추후에 전체 수정 필요
t = datetime.datetime.now()
filter_list = ["페미","냄져","한남"]

#확장 필요
db_name = 'pookle'
ip = 'localhost'
port = 27017

def db_manage(mode, coll_name = None, doc = None, is_first = None):
	db = db_access()
	if coll_name != None and mode != "renewal_date":
		coll = db[coll_name]
	else:
		coll = db['recent_date']
	

	if mode == "add":
		addok = 0
		for i in doc:
			cnt = 0
			for j in coll.find({'title':i['title']},\
									{'_id':0,'title':1}).\
										sort([("date", -1)]):
				if i['title'] == j['title']:
					cnt = 1
					print("중복처리: ",i['title'])
					break

			for j in filter_list:
				if i["title"].find(j) != -1:
					print("부적합 게시물: ",i['title'])
					cnt = 1
					break

			if cnt == 0:
				# i 변수가 하나의 게시물
				# 여기다가 추가하고픈 게시물의 원하는 칼럼 붙여넣으면 됨 
				# ex) i.update({"추가할 항목":"추가할 값"})
				addok += 1
				coll.insert(i)
			else:
				continue

		return addok


	elif mode == "renewal_date":
		if is_first == True:
			db['recent_date'].insert(doc)
		else:
			db['recent_date'].update({"name":coll_name}, doc)


	elif mode == "get_recent":
		return db['recent_date'].find_one({"name":coll_name})


def db_access():
	client = pymongo.MongoClient(ip,port)
	db = client[db_name]
	return db

	
	
	 	

	 



