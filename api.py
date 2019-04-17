import tornado.ioloop
import tornado.web
import subprocess
from tornado.escape import json_decode
from notebook_recommender import setup, querySchema

ix = None
PORT = 8000

class MainHandler(tornado.web.RequestHandler):
    def output_notebooks(self, me, query):
        if (ix is None):
            return
        notebooks = querySchema(ix, query)
        me.write({"notebooks": notebooks})

    async def get(self):
        keyword = self.get_argument("keyword", "", True)
        self.output_notebooks(self, keyword)

    async def post(self):
        body = json_decode(self.request.body)
        keyword = body["keyword"] if "keyword" in body else ""
        self.output_notebooks(self, keyword)

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
