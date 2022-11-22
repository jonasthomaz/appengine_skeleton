from webapp2 import WSGIApplication, Route
from skeleton.domain.handlers.home import HomeHandler

app = WSGIApplication([
    Route("/", HomeHandler),
], debug=True)
