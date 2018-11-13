import json

import tornado.web as web

import wikipedia


def searchResults(lang, search):
	wikipedia.set_lang(lang)
	s = wikipedia.search(search)
	return s


def allLanguages():
	return list(wikipedia.languages().keys())


class SearchController(web.RequestHandler):

	def data_received(self, chunk):
		pass

	def get(self):
		lang = self.get_argument('l')
		search = self.get_argument('s')

		self.set_header("Content-Type", 'application/json; charset="utf-8"')
		self.finish(json.dumps(searchResults(lang, search), ensure_ascii=False))


class LanguagesController(web.RequestHandler):

	def data_received(self, chunk):
		pass

	def get(self):
		self.set_header("Content-Type", 'application/json; charset="utf-8"')
		ls = allLanguages()
		self.finish(json.dumps(ls, ensure_ascii=False))
