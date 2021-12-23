"""Importing modules"""
import falcon
import json

from falcon.http_status import HTTPStatus
from wsgiref import simple_server
from datastore import ITEMS

class RootResource():
   def on_get(self,req, resp):
            """Handles main server request to pass test"""
            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass

class GetResource:
    def on_get(self, req, resp, itemId):
        """Handles GET request """
        if req.get_param("id"):
            resp.media = {'user_id': "", "keywords":"","description": "", "lat": "" , "lon": "" }
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


class DeleteResource:
    def on_delete(self, req, resp):
        """Handles DELETE request """
        resp.media = req.media
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON


"""Enable CORS policy for example.com and allows credentials"""
app = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='example.com', allow_credentials='*'))

app = application = falcon.App()
app.add_route('/item/{itemId}/', GetResource())
app.add_route('/items/', GetManyResource())
app.add_route('/item/', PostResource())
app.add_route('/item/{itemId}/', DeleteResource())
app.add_route('/', RootResource())


if __name__ == '__main__':

    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8000, app)
    try:
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass