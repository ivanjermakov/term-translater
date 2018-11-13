from pyquery import PyQuery


def languages(url):
	html = PyQuery(url)
	links = html('a.interlanguage-link-target')

	langs = [l.attrib['lang'] for l in links]
	hrefs = [l.attrib['href'] for l in links]

	return {key: value for (key, value) in zip(langs, hrefs)}


def pageTitle(url):
	html = PyQuery(url)
	title = html('h1#firstHeading')
	return title.text()
