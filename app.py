import tornado.ioloop
import tornado.web
from tornado.web import url
from tornado.options import define, options
import os
import dbase
import config


pages = config.pages


class MainHendler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', title = config.home_page['title'], pages = pages)


class PageHandler(tornado.web.RequestHandler):
    def get(self, page_n):
        records = dbase.Dbase()
        rr = records.fetchAll(pages[page_n]['request'])
        self.render('page.html', title = pages[page_n]['title'], page_n = pages[page_n]['title'], head_table = pages[page_n]['head_table'],  data = rr)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r"/",MainHendler, name="home"),
            url(r"/(?P<page_n>[A-Za-z]+)/$", PageHandler, name="page"),
        ]
        settings = dict(
            template_path   = config.template_path,
            static_path     = config.static_path,
        )
        
        tornado.web.Application.__init__(self,handlers,**settings)

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8887)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()