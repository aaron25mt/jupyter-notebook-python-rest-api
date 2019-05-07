import tornado.ioloop
import tornado.web
import subprocess
import os
from notebook_recommender import setup, querySchema

ix = None
PORT = 8001

notebooks_path_dir = os.path.join(os.path.dirname(__file__), "notebooks")

class MainHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')

    async def get(self):
        if (ix is None):
            return
        keyword = self.get_argument("keyword", None, True)
        notebooks = querySchema(ix, keyword)
        self.write({"notebooks": notebooks})

    def options(self):
        self.set_status(204)
        self.finish()

def make_app():
    return tornado.web.Application([
        (r"/api/rec/jupyter", MainHandler),
        (r'/notebooks/(.*)', tornado.web.StaticFileHandler, {'path': notebooks_path_dir}),
    ])

if __name__ == "__main__":
    app = make_app()
    ix = setup()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
    print(f"Server running on port {PORT}")
