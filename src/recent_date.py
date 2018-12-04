def get_recent_date(URL, db_docs):
	recent_doc = db_docs[0]

	if len(db_docs) >= 2:
		for doc in db_docs[1:]:
			if recent_doc['date'] < doc['date']:
				recent_doc = doc

	recent_date = {"name":URL['info'], "title":recent_doc['title']\
							, "recent_date":recent_doc['date']}

	return recent_date


def get_today():
	import datetime

	now = datetime.datetime.now()
	date = now.strftime("%Y-%m-%d %H:%M:%S")

	return date
