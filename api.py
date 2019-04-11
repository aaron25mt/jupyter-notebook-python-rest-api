import tornado.ioloop
import tornado.web
import subprocess
from notebook_recommender import setup, querySchema

ix = None
PORT = 8000

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        if (ix is None):
            return
        keyword = self.get_argument("keyword", None, True)
        notebooks = querySchema(ix, keyword)
        self.write({"notebooks": notebooks})

def make_app():
    return tornado.web.Application([
        (r"/api/rec/jupyter", MainHandler),
    ])
if __name__ == "__main__":
    app = make_app()
    ix = setup()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
    print(f"Server running on port {PORT}")