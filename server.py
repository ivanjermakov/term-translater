import tornado.ioloop
import tornado.web as web

from search import SearchController, LanguagesController
from translate import TranslateController


def make_app():
	return web.Application([
		(r'/t', TranslateController),
		(r'/s', SearchController),
		(r'/a', LanguagesController),
		(r"/(.*)", tornado.web.StaticFileHandler, {'path': 'static/', 'default_filename': 'index.html'}),
	])


def start():
	app = make_app()
	app.listen(80)
	tornado.ioloop.IOLoop.current().start()
