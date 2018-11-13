import json

from tornado import web
import wikipedia
import wikiparse


class TranslateController(web.RequestHandler):

	def data_received(self, chunk):
		pass

	def get(self):
		fromLang = self.get_argument('from')
		toLang = self.get_argument('to')
		title = self.get_argument('title')

		wikipedia.set_lang(fromLang)
		page = wikipedia.page(title)
		wikipedia.set_lang(toLang)

		translatedPages = wikiparse.languages(page.url)

		self.finish(wikiparse.pageTitle(translatedPages[toLang]))
