from bs4 import BeautifulSoup
from url_parser import URLparser
# 부경대 공지사항 목록
import PK_main 
import PK_ce
import PK_pknu
import PK_today
import PK_pknu_lecture
import PK_pknulogin
import PK_dorm
import PK_start
import PK_dcinside
import PK_coop
import PK_sh
import PK_duem
import PK_ee
import PK_eelogin
import PK_aquacul
import PK_physics
import PK_chem
import PK_dba
import PK_english

duemlist = ['duem','korean','japan','job','history','economic',\
'pknulaw','pknupa','chinese','masscom','politics','education','visual',\
'industrial','fashion','marinesports','pknudic','archieng','pknuarchi','fire',\
'pknusme','itcae','imagesys','electric','control','induseng','env','oceaneng','pkuocean',\
'earth','envatm','msce']
eelist = ['ee','ice','me','mae','ref']
aquacullist = ['aquacul','mpsm','mbe','fedu','marinebio','nulife','aquamed','mse']
phlist = ['physics','microbiology','stat','math','nursing']

def Crawling(target, URL, is_first):
	select = URL['info'].split('_')[1]

	try:
		driver = URLparser(URL['url'])
	except Exception as e:
		print("Connect Error")
		return

	if driver == None:
		return

	if target == 'PK_univ':
		print('-------------------------------------')
		print('Selected <' + URL['info'] +'>')
		print('-------------------------------------')
		
		if select == 'main':
			PK_main.parsing(driver, URL, is_first)
		elif select == 'ce':
			PK_ce.parsing(driver, URL, is_first)
		elif select == 'pknu':
			PK_pknu.parsing(driver, URL, is_first)
		elif select == 'today':
			PK_today.parsing(driver, URL, is_first)
		elif select == 'pknulec' and is_first == True:
			PK_pknu_lecture.parsing(driver, URL, is_first)
		elif select == 'pknulogin':
			PK_pknulogin.parsing(driver, URL, is_first)
		elif select == 'dorm':
			PK_dorm.parsing(driver, URL, is_first)
		elif select == 'start':
			PK_start.parsing(driver, URL, is_first)
		elif select == 'dcinside':
			PK_dcinside.parsing(driver, URL, is_first)
		elif select == 'coop':
			PK_coop.parsing(driver, URL, is_first)
		elif select == 'sh':
			PK_sh.parsing(driver, URL, is_first)
		elif select in duemlist:
			PK_duem.parsing(driver, URL, is_first)
		elif select in eelist:
			PK_ee.parsing(driver, URL, is_first)
		elif select == 'eelogin':
			PK_eelogin.parsing(driver, URL, is_first)
		elif select in aquacullist:
			PK_aquacul.parsing(driver, URL, is_first)
		elif select in phlist:
			PK_physics.parsing(driver, URL, is_first)
		elif select == 'chem':
			PK_chem.parsing(driver, URL, is_first)
		elif select == 'dba':
			PK_dba.parsing(driver, URL, is_first)
		elif select == 'english':
			PK_english.parsing(driver, URL, is_first)

