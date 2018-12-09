import pymongo 
import time
db_name = 'pookle'
ip = 'localhost'
port = 27017

def Search(db, text):
	from operator import itemgetter
	result = []
	text_list = text.split(" ")

	if any(len(element) <= 1 for element in text_list):
		return None

	for element in text_list:

		for col in db.collection_names():
			if col.startswith("PK_") == False:
				continue

			coll_list = list(db[col].find({"$or":[{"title":{"$regex":element}},\
													{"tag":{"$elemMatch": {"$regex":element }}},\
													{"post":{"$regex":element}}\
													]}))

			for i in coll_list:
				if any( i["_id"] == j["_id"] for j in result):
					for j in result:
						if j['_id'] == i['_id']:
							if j['title'].find(element) != -1:
								j["score"] += 2
							if type(j['post']) is str and j['post'].find(element) != -1:
								j["score"] += 1
							for tag in j['tag']:
								if tag.find(element) != -1:
									j["score"] += 1
									break
							j['element'].add(element)
				else:
					i.update({"score":0})
					if i['title'].find(element) != -1:
						i["score"] += 2
					if type(i['post']) is str and i['post'].find(element) != -1:
						i["score"] += 1
					for tag in i['tag']:
						if tag.find(element) != -1:
							i["score"] += 1
							break
					i.update({"element":set([element])})
					result.append(i)

	for i in result:
		i['score'] += len(i['element'])*4

	result = sorted(result, key=itemgetter('score','fav_cnt',"view",'date'),reverse = True)
	return result

def db_access():
	client = pymongo.MongoClient(ip,port)
	db = client[db_name]
	return db

if __name__ == '__main__':

	n = input("Search: ")
	start_time = time.time()
	db = db_access()
	List = Search(db,n)
	end_time = time.time() - start_time
	# 검색창이공백일때 예외처리
	# 검색어는 무조건 2글자 이상의 단어가 포함되야 함
	if(List != None):
		print(List)
		print()
		if len(List) >= 4:
			print("This is Top4")
			print(List[0])
			print(List[1])
			print(List[2])
			print(List[3])
		print(len(List))
		print(end_time)
	else:
		print("2글자 이상의 단어로만 이루어져야 합니다")
