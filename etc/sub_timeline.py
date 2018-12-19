import pymongo 
import datetime
from operator import itemgetter
from random import shuffle, randrange

now = datetime.datetime.now() - datetime.timedelta(days = 15)
date = now.strftime("%Y-%m-%d %H:%M:%S")

include_coll = [
	#메인
	["PK_main_notice","PK_main_free","PK_main_openmarket","PK_main_boarding",
	"PK_main_lost","PK_main_car","PK_pknu_bamboo","PK_pknu_public","PK_pknu_lost",
	"PK_pknu_free","PK_pknu_twinkle","PK_pknu_kin","PK_today_today",
	"PK_pknulogin_market","PK_dorm_notice","PK_dcinside_free", "PK_sh_notice",\
	"PK_start_notice"],
	#진로
	["PK_job","_jobinfo","_samsungsw","PK_start","_notice","PK_main_free",
	"PK_duem_free",'PK_industrial_free',"PK_ee_free","PK_mae_free"],
	#스터디&모임
	['PK_main_circle',"PK_pknu_moim","PK_main_volunteer","_notice","_public",
	"PK_main_free","PK_duem_free",'PK_industrial_free',"PK_ee_free","PK_mae_free"],
	#알바&구인
	["_parttimejob","_public","_notice","_circle","PK_main_free"],
	#행사&대외활동
	["PK_main_free","PK_duem_free",'PK_industrial_free',"PK_ee_free",
	"PK_mae_free","_competition","PK_job_education","_notice",
	"PK_start_free"]
	]
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

db_name = 'pookle'
ip = 'localhost'
port = 27017

def db_access():
	client = pymongo.MongoClient(ip,port)
	db = client[db_name]
	return db

def View(db, icoll, itag, etag):
	
	result = []

	for col in db.collection_names():
		if any(icol in col for icol in icoll) == False:
			continue
		#메인타임라인의 경우 타학과공지 제외
		coll_list = list(db[col].find(
													{"$and":[
															{"tag":{ "$in": itag }},	
															{"tag":{"$nin":etag }},
															{"date":{"$gt":date}}
														]
													}))
		#2달이내의 글만 갖고옴
		result += coll_list

	fav_list = sorted(result, key=itemgetter("fav_cnt","view","date"), reverse = True)
	shuffle(result)
	fav_cnt = 0

	for i in range(len(result)):
		if i >= 240 or fav_cnt >= 80:
			break
		if randrange(100) <= 40 \
		and any(fav_list[fav_cnt] == j["_id"] for j in result[0:i]) == False:
			result.insert(i, fav_list[fav_cnt])
			fav_cnt += 1
		elif any(result[i]["_id"] == j["_id"] for j in result[0:i]):
			del result[i]
	return result


if __name__ == '__main__':
	import time

	start_time = time.time()
	db = db_access()
	List =View(db, include_coll[4], include_tag[4], exclude_tag)
	end_time = time.time() - start_time

	for i in range(10):
		print(List[i]['title'])
		print(List[i]['tag'])
		print(List[i]['date'])
		print(List[i]['fav_cnt'])
	print(len(List))
	print(end_time)