# Unused sources for now

from bs4 import BeautifulSoup, Tag, NavigableString
import sys

def clone(el):
    if isinstance(el, NavigableString):
        return type(el)(el)

    copy = Tag(None, el.builder, el.name, el.namespace, el.nsprefix)
    copy.attrs = dict(el.attrs)
    for attr in ('can_be_empty_element', 'hidden'):
        setattr(copy, attr, getattr(el, attr))
    for child in el.contents:
        copy.append(clone(child))
    return copy

def text_parsing(bs0bj, domain):
	children = bs0bj.findChildren(recursive = False)
	content = ""

	if not children:
		return ""

	for tag in children:
		if tag.get('src') != None:
			content += ("\n<태그>: " + tag.name + "\n")
			content += ("src: " + domain + tag.attrs['src'] + "\n")
			content += ("</태그>\n" + "\n")

		if tag.get('href') != None:
			content += ("\n<태그>: " + tag.name + "\n")
			content += ("src: " + domain + tag.attrs['href'] + "\n")
			content += ("태그 내용:", tag.get_text() + "\n")
			content += ("</태그>\n" + "\n")
		
		tag_text = clone(tag)
		for i in tag_text.find_all():
			i.decompose()
		content += tag_text.get_text()

		return content + text_parsing(tag, domain)

if __name__ == '__main__':
	text_parsing(bs0bj,domain)