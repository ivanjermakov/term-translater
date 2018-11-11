import json

import tornado.web as web

import wikipedia


def searchResults(lang, search):
	wikipedia.set_lang(lang)
	return wikipedia.search(search)


class SearchController(web.RequestHandler):

	def data_received(self, chunk):
		pass

	def get(self):
		lang = self.get_argument('l')
		search = self.get_argument('s')

		self.write(searchResults(lang, search))
		self.content_type = 'application/json'
