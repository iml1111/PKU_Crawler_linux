def slang_filter(text):
	import re
	filter_list = ["페미","냄져","한남","씨발",'섹스','개년','애미','애비','창녀','홍어','후빨'
			,'셋스','시발','보지','잠지','모텔','등신','빨통',"씨팔",'니미','엠창','틀딱','응디','놈현'
			,'느금','창년','걸레','보빨','니엄','콘돔',"걸레",'병신','빙신','갈보','섻스','쎅스','ㅅㅂ','ㅈㄹ'
			,'족같','붕알','부랄','무현','ㅆㅂ','ㅆ발','니앰','니엄','색기' ,'씨팔']

	for i in filter_list:
		r1 = re.search(i,text)
		r2 = re.search(i[0] + "." + i[1],text)
		r3 = re.search(i[0] + ".." + i[1],text)
		r4 = re.search(i[0] + "..." + i[1],text)
		if r1 or r2 or r3 or r4:
			return True
	return False
	