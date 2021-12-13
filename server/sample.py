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
api.add_route('/quote', QuoteResource())
api = falcon.API()




class GetResource:
    def on_get(self, req, resp):
        """Handles GET request """
        if req.get_param("id"):
            resp.media = {'user_id': "", "keywords":"","description": "", "lat": "" , "lon": "" }
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON

class PostResource:
    def on_post(self, req, resp):
        """Handles POST request """

        resp.media = {"id" : ITEMS.id, 'user_id' : ITEMS.user_id, 'description' : ""}
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON


class DeleteResource:
    def on_delete(self, req, resp):
        """Handles DELETE request """
        resp.media = req.media
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON




app = application = falcon.App()
app.add_route('/post/item', PostResource())
app.add_route('/item/{itemId}/', GetResource())
api.add_route('/delete', DeleteResource())



if __name__ == '__main__':

    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8000, api)
    try:
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass