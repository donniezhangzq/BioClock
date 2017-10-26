#!/usr/bin/env python
# -*- encoding=utf8 -*-
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options

define("port", default=8080, help="port to listen", type=int)
define("debug", default=True, help="run in debug mode")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ZhiHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("zhi.html")

class XingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("xing.html")

def make_app():
    return tornado.web.Application([
            (r"/", IndexHandler),
            (r"/zhi", ZhiHandler),
            (r"/xing", XingHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
        )

if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
