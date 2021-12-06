import falcon
import json

from wsgiref import simple_server
from dataStore import ITEMS

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote






class ItemResource:
    def on_get(self, req, resp):
        """Handles GET request """
        if req.get_param("user_id"):
            resp.media = {'user_id': "", "keywords":"","description": "", "lat": "" , "lon": "" }
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON

api = falcon.API()
app = application = falcon.App()
app.add_route('/get', ItemResource())
api.add_route('/quote', QuoteResource())



if __name__ == '__main__':

    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8000, api)
    try:
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass