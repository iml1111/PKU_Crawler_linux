def post_wash(text):
	data = ""
	for i in range(len(text)-1):
		if text[i] == '\n' or text[i] == '\r'  or text[i] == '\xa0' or text[i] == '\uf06d':
			continue
		if text[i] == '\\' and (text[i+1] == 'n' or text[i+1] == 'r'):
			continue
		elif (text[i] == 'n' or text[i] == 'r') or text[i-1] == '\\':
			continue
		data = data + text[i]

	return data