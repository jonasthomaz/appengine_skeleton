from webapp2 import RequestHandler

class HomeHandler(RequestHandler):

    def get(self):
        return self.sendJson({
            "message": "Welcome to the API"
        })
