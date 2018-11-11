import tornado.ioloop
import tornado.web as web

from search import SearchController


def make_app():
	return web.Application([
		# (r"/(.*)", tornado.web.StaticFileHandler, {'path': './files', 'default_filename': 'index.html'}),
		(r'/s', SearchController),
	])


def start():
	app = make_app()
	app.listen(80)
	tornado.ioloop.IOLoop.current().start()
