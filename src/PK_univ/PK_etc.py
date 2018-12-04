from db_manager import db_manage
from recent_date import get_today

today = get_today()

List = [

{"url":"http://dormitory.pknu.ac.kr/03_notice/notice01.php",
	"title":"학생생활관 오늘의 식단",
	"post":"식사는 카드인식 후 가능하며, 자율배식으로 합니다.\
	식사예절 준수, 용모, 복장을 단정히 하고 건강을 위해 끼니를 거르지 않고\
	규칙적으로 식사하도록 합시다.",
	"date":today,
	'tag':["기숙사","사이트"]},

{"url":"http://lms.pknu.ac.kr/ilos/main/main_form.acl",
	"title":"부경대학교 - LMS",
	"post":"학사일정 및 강의관련 공지사항 등을 확인하실 수 있습니다.",
	"date":today,
	'tag':["기타","사이트"]},

{"url":"https://ebook.pknu.ac.kr/FxLibrary/",
	"title":"부경대학교 전자책 도서관",
	"post":"여러 분야에 관련된 책을 대여할 수 있습니다.",
	"date":today,
	'tag':["기타","사이트"]},

{"url":"http://lms.pknu.ac.kr/ilos/main/main_form.acl",
	"title":"부경대학교 학사일정",
	"post":"부산광역시 남구 용소로 45(608-737)본관 503호 기초교양교육원 TEL. 051-629-6947 FAX. 051-629-6949",
	"date":today,
	'tag':["기타","사이트"]},

{"url":"http://cms.pknu.ac.kr/counseling/main.do",
	"title":"부경대학교 학생상담센터",
	"post":"인생의 든든한 동반자 부경대학교 학생상담센터 부산광역시 남구 용소로 45, 부경대학교 대연캠퍼스 동원 장보고관 3층 학생상담센터 (대연동) TEL:(051)629-6763~5 FAX:(051)629-6766",
	"date":today,
	'tag':["기타","사이트"]},

{"url":"http://cms.pknu.ac.kr/counseling/main.do",
	"title":"부경대학교 자료실",
	"post":"필요한 자료를 올리고 다운받아가세요. 여러분이 올려주시는 자료는 많은 도움이 됩니다.",
	"date":today,
	'tag':["기타","사이트"]},

{"url":"http://cms.pknu.ac.kr/duem/main.do",
	"title":"부경대학교 글로벌자율전공학부",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 웅비관 3층 1318호 TEL:051-629-5650~1 FAX:051-629-5651",
	"date":today,
	'tag':["글로벌자율전공학부","사이트"]},

{"url":"http://cms.pknu.ac.kr/korean/main.do",
	"title":"부경대학교 국어국문학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 인문사회과학대학 국어국문학과 TEL:051)629-5405 FAX:051)629-5408",
	"date":today,
	'tag':["국어국문학과","사이트"]},

{"url":"http://ce.pknu.ac.kr/main/main.php",
	"title":"부경대학교 컴퓨터공학과",
	"post":"부산광역시 남구 용소로 45 부경대학교 대연캠퍼스 누리관(A13) 2223호 TEL 051-629-6260(대학원),   6261(학과),   7805(SST, SCSC) │ FAX 051-629-6264",
	"date":today,
	'tag':["컴퓨터공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/japanese/main.do",
	"title":"부경대학교 일어일문학부",
	"post":"부산광역시 남구 용소로 45, 인문사회경영관(C25) 일어일문학부(1412호) (대연동) TEL: 051-629-5390 FAX: 051-629-5393",
	"date":today,
	'tag':["일어일문학부","사이트"]},

{"url":"http://cms.pknu.ac.kr/history/main.do",
	"title":"부경대학교 사학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 인문사회·경영관(C25) 1209호 사학과 사무실 TEL:629-5422~3 FAX:629-5425",
	"date":today,
	'tag':["사학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/economic/main.do",
	"title":"부경대학교 경제학부",
	"post":"(48513) 부산광역시 남구 용소로 45 부경대학교 대연캠퍼스 인문사회경영관 828호 경제학부 사무실(부경대학교 인문사회과학대학 경제학부) TEL:629-5310,5312 FAX:629-5315",
	"date":today,
	'tag':["경제학부","사이트"]},

{"url":"http://cms.pknu.ac.kr/pknulaw/main.do",
	"title":"부경대학교 법학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 인문사회경영동 441호 법학과사무실 TEL: 051)629-5435~6 FAX: 051)629-5438",
	"date":today,
	'tag':["법학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/pknupa/main.do",
	"title":"부경대학교 행정학과",
	"post":"부산광역시 남구 용소로 45, C25-926호 행정학과사무실 (대연동) TEL:051-629-5450 FAX:051-629-5453",
	"date":today,
	'tag':["행정학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/chinese/main.do",
	"title":"부경대학교 중국학과",
	"post":"부산광역시 남구 용소로 45, C25(인문관) 626호 중국학과사무실 (대연동) TEL:051-629-7050 FAX:051-629-7051",
	"date":today,
	'tag':["중국학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/masscom/main.do",
	"title":"부경대학교 신문방송학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 인문사회관 신문방송학과 TEL:629-5475 FAX:629-5478",
	"date":today,
	'tag':["신문방송학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/politics/main.do",
	"title":"부경대학교 정치외교학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 인문사회경영관 216호 TEL:629-5465 FAX:629-5468",
	"date":today,
	'tag':["정치외교학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/education/main.do",
	"title":"부경대학교 유아교육과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 인문사회·경영관 547호 메일주소: 407070@pknu.ac.kr TEL:629-5490 FAX:629-5493",
	"date":today,
	'tag':["유아교육과","사이트"]},

{"url":"http://cms.pknu.ac.kr/visual/main.do",
	"title":"부경대학교 시각디자인학과",
	"post":"부산광역시 남구 용소로 45, 디자인관(A22) 104호 시각디자인학과사무실 (대연동) TEL:051-629-5350 FAX:051-629-5353",
	"date":today,
	'tag':["시각디자인학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/industrial/main.do",
	"title":"부경대학교 공업디자인학과",
	"post":"부산광역시 남구 용소로 45, A22(디자인관) 104(학과사무실) (대연동) TEL:051-629-5351 FAX:0516295353",
	"date":today,
	'tag':["공업디자인학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/fashion/main.do",
	"title":"부경대학교 패션디자인학과",
	"post":"부산광역시 남구 용소로 45, 나래관(A23) 605호 패션디자인학과사무실 (대연동) TEL:051-629-5352 FAX:051-629-5354",
	"date":today,
	'tag':["패션디자인학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/marinesports/main.do",
	"title":"부경대학교 해양스포츠학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 7호관 7322호 TEL:051-629-5630 FAX:051-629-5634",
	"date":today,
	'tag':["해양스포츠학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/pknudic/main.do",
	"title":"부경대학교 국제통상학부",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 경영대학 국제통상학부 사무실 TEL:629-5750~1 FAX:629-5754",
	"date":today,
	'tag':["국제통상학부","사이트"]},

{"url":"https://cms.pknu.ac.kr/archieng/main.do",
	"title":"부경대학교 건축공학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 8호관(C22) 430호 건축공학과사무실 TEL:051-629-6082 FAX:051-629-7084",
	"date":today,
	'tag':["건축공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/pknuarchi/main.do",
	"title":"부경대학교 건축학과",
	"post":"부산광역시 남구 용소로 45, C22호(건축관) 3층 332호 건축학과사무실 (대연동) TEL:051-629-6080 FAX:051-629-7083",
	"date":today,
	'tag':["건축학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/fire/main.do",
	"title":"부경대학교 소방공학과",
	"post":"부산광역시 남구 용소로 45, C22호(건축관) 3층 332호 건축학과사무실 (대연동) TEL:051-629-6080 FAX:051-629-7083",
	"date":today,
	'tag':["소방공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/pknusme/main.do",
	"title":"부경대학교 시스템경영공학부",
	"post":"부산광역시 남구 용소로 45, 가온관(B21) 618호 (대연동) TEL:051-629-6475~6 FAX:051-629-6478",
	"date":today,
	'tag':["시스템경영공학부","사이트"]},

{"url":"http://cms.pknu.ac.kr/itcae/main.do",
	"title":"부경대학교 IT융합응용공학과",
	"post":"부산광역시 남구 용소로 45, 부경대학교 대연캠퍼스 웅비관(A12) 1307호실 (대연동) TEL:629-6262,6263 FAX:051-629-6230",
	"date":today,
	'tag':["IT융합응용공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/imagesys/main.do",
	"title":"부경대학교 융합디스플레이공학과",
	"post":"부산광역시 남구 용소로 45, 부경대학교 대연캠퍼스 웅비관(A12) 1307호실 (대연동) TEL:629-6262,6263 FAX:051-629-6230",
	"date":today,
	'tag':["융합디스플레이공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/electric_eng/main.do",
	"title":"부경대학교 전기공학과",
	"post":"부산광역시 남구 용소로 45, 가온관(B21) 306호 (대연동) TEL:051-629-6306 FAX:051-629-6305",
	"date":today,
	'tag':["전기공학과","사이트"]},

{"url":"https://cms.pknu.ac.kr/control/main.do",
	"title":"부경대학교 제어계측공학과",
	"post":"부산광역시 남구 용소로 45, 가온관(B21) 410호 (대연동) TEL:051-629-6307 FAX:051-629-6333",
	"date":today,
	'tag':["제어계측공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/induseng/main.do",
	"title":"부경대학교 공업화학과",
	"post":"부산광역시 남구 용소로 45, 가온관(B21) 410호 (대연동) TEL:051-629-6307 FAX:051-629-6333",
	"date":today,
	'tag':["공업화학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/env_eng/main.do",
	"title":"부경대학교 환경공학과",
	"post":"부산광역시 남구 용소로 45, 충무관(B13) 4212호 환경공학과사무실 (대연동) TEL:0516296520 FAX:0516296523",
	"date":today,
	'tag':["환경공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/oceaneng/main.do",
	"title":"부경대학교 해양공학과",
	"post":"부산광역시 남구 용소로 56-1, 부경대학교 해양공학과 (대연동) TEL:6592,6580 FAX:6590",
	"date":today,
	'tag':["해양공학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/pkuocean/main.do",
	"title":"부경대학교 해양학과",
	"post":"부산광역시 남구 용소로 45(대연동 부경대학교대연캠퍼스) 해양공동연구관 115호 TEL:629~6565~6 FAX:629~6568",
	"date":today,
	'tag':["환경학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/earth/main.do",
	"title":"부경대학교 지구환경과학과",
	"post":"부산광역시 남구 용소로 45, 부경대학교 대연캠퍼스 환경해양관(B14) 415호 지구환경과학과 (대연동) TEL:051-629-6621 FAX:051-629-6623",
	"date":today,
	'tag':["지구환경과학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/envatm/main.do",
	"title":"부경대학교 환경대기과학과",
	"post":"부산광역시 남구 용소로 45, 부경대학교 대연캠퍼스 충무관(B13) 4308A호 환경대기과학과 (대연동) TEL:051-629-6635~6 FAX:051-629-6638",
	"date":today,
	'tag':["환경대기과학과","사이트"]},

{"url":"http://cms.pknu.ac.kr/msce/main.do",
	"title":"부경대학교 기계조선융합공학과",
	"post":"부산광역시 남구 용소로 45, 향파관 410-2호 (대연동) TEL:051-629-6596 FAX:051-629-6599",
	"date":today,
	'tag':["기계조선융합공학과","사이트"]},

{"url":"http://food.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 식품공학과",
	"post":"부경대학교 식품공학과 홈페이지",
	"date":today,
	'tag':["식품공학과","사이트"]},

{"url":"http://aqua-culture.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 해양바이오신소재학과",
	"post":"부경대학교 해양바이오신소재학과 홈페이지",
	"date":today,
	'tag':["해양바이오신소재학과","사이트"]},

{"url":"http://mpsm.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 해양생산시스템관리학부",
	"post":"부경대학교 해양생산시스템관리학부 홈페이지",
	"date":today,
	'tag':["해양생산시스템관리학부","사이트"]},	

{"url":"http://mbe.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 해양수산경영학과",
	"post":"부경대학교 해양수산경영학과 홈페이지",
	"date":today,
	'tag':["해양수산경영학과","사이트"]},

{"url":"http://fedu.pknu.ac.kr/sub06/sub01.asp?Bid=notice",
	"title":"부경대학교 수해양산업교육과",
	"post":"부경대학교 수해양산업교육과 홈페이지",
	"date":today,
	'tag':["수해양산업교육과","사이트"]},

{"url":"http://fedu.pknu.ac.kr/sub06/sub01.asp?Bid=notice",
	"title":"부경대학교 수해양산업교육과",
	"post":"부경대학교 수해양산업교육과 홈페이지",
	"date":today,
	'tag':["수해양산업교육과","사이트"]},
	
{"url":"http://marinebio.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 자원생물학과",
	"post":"부경대학교 자원생물학과 홈페이지",
	"date":today,
	'tag':["자원생물학과","사이트"]},

{"url":"http://nulife.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 식품영양학과",
	"post":"부경대학교 식품영양학과 홈페이지",
	"date":today,
	'tag':["식품영양학과","사이트"]},

{"url":"http://aquamed.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 수산생명의학과",
	"post":"부경대학교 수산생명의학과 홈페이지",
	"date":today,
	'tag':["수산생명의학과","사이트"]},
	
{"url":"http://mse.pknu.ac.kr/main/main.asp",
	"title":"부경대학교 기계시스템공학과",
	"post":"부경대학교 기계시스템공학과 홈페이지",
	"date":today,
	'tag':["기계시스템공학과","사이트"]},

{"url":"http://nursing.pknu.ac.kr/kor/main/main.php",
	"title":"부경대학교 간호학과",
	"post":"부경대학교 간호학과 홈페이지",
	"date":today,
	'tag':["간호학과","사이트"]},

{"url":"http://physics.pknu.ac.kr/main/main.php",
	"title":"부경대학교 물리학과",
	"post":"부경대학교 물리학과 홈페이지",
	"date":today,
	'tag':["물리학과","사이트"]},

{"url":"http://microbiology.pknu.ac.kr/main/main.php",
	"title":"부경대학교 미생물학과",
	"post":"부경대학교 미생물학과 홈페이지",
	"date":today,
	'tag':["미생물학과","사이트"]},

{"url":"http://stat.pknu.ac.kr/kor/main/main.php",
	"title":"부경대학교 통계학과",
	"post":"부경대학교 통계학과 홈페이지",
	"date":today,
	'tag':["통계학과","사이트"]},

{"url":"http://math.pknu.ac.kr/kor/main/main.php",
	"title":"부경대학교 응용수학과",
	"post":"부경대학교 응용수학과 홈페이지",
	"date":today,
	'tag':["응용수학과","사이트"]},

{"url":"http://chem.pknu.ac.kr/home",
	"title":"부경대학교 화학과",
	"post":"부경대학교 화학과 홈페이지",
	"date":today,
	'tag':["화학과","사이트"]},

{"url":"http://dba.pknu.ac.kr/",
	"title":"부경대학교 경영학부",
	"post":"부경대학교 경영학부 홈페이지",
	"date":today,
	'tag':["경영학부","사이트"]},

{"url":"http://english.pknu.ac.kr/ko_home",
	"title":"부경대학교 영어영문학부",
	"post":"부경대학교 영어영문학부 홈페이지",
	"date":today,
	'tag':["영어영문학부","사이트"]},
]

def crawling():
	db_manage("add","PK_etc",List)

