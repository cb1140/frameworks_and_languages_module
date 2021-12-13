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

"""Enable CORS policy for example.com and allows credentials"""
app = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='example.com', allow_credentials='*'))



class GetResource:
    def on_get(self, req, resp):
        """Handles GET request """
        if req.get_param("id"):
            resp.media = {'user_id': "", "keywords":"","description": "", "lat": "" , "lon": "" }
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON

            fields = set(("user_id","keywords","description", "lat", "lon"))

        """Returns right HTTP protocol if items cannot be found"""
        if ITEMS.keys != fields:
            resp.status = HTTP_204
        else:
            ITEMS[new_id] = req.json
            ITEMS.add()
            resp.status = falcon.HTTP_201




        
class GetManyResource():
   def on_get(self,req, resp):
       
            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass

class PostResource:
    def on_post(self, req, resp):
        """Handles POST request """


        resp.media = {"id" : ITEMS.id, 'user_id' : ITEMS.user_id, 'description' : ""}
        resp.status = falcon.HTTP_201
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