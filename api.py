import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # parse body for functionality & keywords
        # call script with parameters
        # retrieve and format output to specified response
        # return formatted output
        pass

def make_app():
    return tornado.web.Application([
        (r"/api/rec/jupyter", MainHandler),
    ])
if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()