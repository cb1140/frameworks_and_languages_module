"""Importing modules"""
import falcon
import json

from falcon.http_status import HTTPStatus
from wsgiref import simple_server
from datastore import ITEMS

class HandleCORSResource(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        resp.set_header('Access-Control-Max-Age', 1728000)
        resp.text = "I love this assignment so much."
        resp.content_type = "text/html"
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_204, text='\n')

class RootResource():
   def on_get(self,req, resp):
            """Handles main server request to pass test"""
            resp.status= falcon.HTTP_204
            resp.content_type = falcon.MEDIA_JSON
            
            

class OptionsResource():
   def on_options(self,req, resp):
            """Handles Option Request"""
            resp.status= falcon.HTTP_204
            resp.content_type = falcon.MEDIA_JSON
            
            

class GetResource:
    def on_get(self, req, resp, itemId):
        """Handles GET request """
        if req.get_param("id"):
            resp.media = {'user_id': "", "keywords":"","description": "", "lat": "" , "lon": "" }
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
    def on_delete(self, req, resp):
        """Handles DELETE request """
        resp.media = req.media
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON

        
class GetManyResource():
   def on_get(self, req, resp, itemId): 
            """Handles GET MANY request """
            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass

class PostResource:
    def on_post(self, req, resp):
        """Handles POST request """
        resp.media = {"id" : ITEMS.id, 'user_id' : ITEMS.user_id, 'description' : ""}
        resp.status = falcon.HTTP_201
        resp.content_type = falcon.MEDIA_JSON

        fields = set(("user_id","keywords","description", "lat", "lon"))
        """Returns right HTTP protocol if items cannot be found"""
        if ITEMS.keys != fields:
            resp.status = HTTP_204
        else:
            ITEMS[new_id] = req.json
            ITEMS.add()
            resp.status = falcon.HTTP_201

#replaces old CORS block
app = application = falcon.API(middleware=[HandleCORSResource()])
app.add_route('/item/{itemId}/', GetResource())
app.add_route('/items/', GetManyResource())
app.add_route('/item/', PostResource())
app.add_route('/', RootResource())


if __name__ == '__main__':

    server = simple_server.make_server("0.0.0.0", 8000, app)
    try:
        
        server.serve_forever()
    except KeyboardInterrupt:
        pass