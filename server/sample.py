"""Importing libraries"""
"""By default Falcon only enables handlers for JSON and HTML"""
import falcon
import json
import datetime

from falcon.http_status import HTTPStatus
from wsgiref import simple_server
from datastore import *

"""Handles OPTIONS and GET Request"""
class RootResource():
   def on_get(self,req, resp):
            """Handles main server request to pass test"""
            resp.status= falcon.HTTP_200
            resp.content_type = "text/html"
            """Fun fact of the day to make sure the server request works"""
            resp.text = "Hoovers were originally horse-drawn."
            print("GET /","-", resp.status)

   def on_options(self,req, resp):
            """Handles Option Request"""
            resp.status= falcon.HTTP_204
            resp.content_type = "text/html" 
            resp.set_header = ('Access-Control-Allow-Methods', 'POST')
            print("OPTIONS /", "-", resp.status)

"""Handles GET and DELETE requests for single items"""            
class GetResource:
    def on_get(self, req, resp, itemId):
        """Handles GET request """
        FetchedItem = {}
        FixedId = int(itemId) - 1
        FetchedItem = datastore.get_item(FixedId)
        
        if not FetchedItem:
            """http.StatusNotFound if no items found"""
            resp.status = falcon.HTTP_404
        else:
             """http.StatusOK"""
             resp.status = falcon.HTTP_200
             resp.media = {
                "id" : FetchedItem.get('id') + 1,
                "user_id" :  FetchedItem.get('user_id'),
                'keywords' :  FetchedItem.get('keywords'),
                'description' :  FetchedItem.get('description'),
                'lat' :  FetchedItem.get('lat'),
                'lon' : FetchedItem.get('lon'),
                
              }
             resp.status = falcon.HTTP_200
             resp.content_type = falcon.MEDIA_JSON

        resp.content_type = "application/json"
        print("GET /item/"+ str(itemId), "-", resp.status)


    def on_delete(self, req, resp, itemId):
        """Handles DELETE request """
        FixedId = int(itemId) - 1
        FetchedItems = datastore.get_item(FixedId)
        
        if not FetchedItems:
            """http.StatusNotFound"""
            resp.status = falcon.HTTP_404
        else:
            """http.StatusCreated"""
            resp.status = falcon.HTTP_201 #should be different but spec mistake? (n)
            datastore.delete_item(FixedId)
            resp.content_type = "application/JSON"
        print("DELETE /item/" + str(itemId), "-", resp.status)


        
class GetManyResource():
   def on_get(self,req, resp):
            """Handles GET MANY request """
            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            ManyItems = max(ITEMS.keys())
            AllItemsList = []
            """DATASTORE.PY """
            for i in range (ManyItems):
                AllItemsList.append(datastore.get_item(i))

            resp.media = {'response' : AllItemsList}
            print("GET /items", "-",)


class PostResource:
    def on_post(self, req, resp):
        """Handles POST request """
        """Creating new dictionary NewData """
        NewData = {}
        NewData = req.get_media()

        """Creating Date From and To, sets date to current time"""
        date_from = datetime.datetime.now()
        date_to = datetime.datetime.now()

        """Sets fields to POST """
        newId = max(ITEMS.keys()) + 1
        resp.media = {'id' : newId}
        RequiredFields = set({'user_id', 'keywords', 'description', 'lat', 'lon'})
        NewFields = set(NewData.keys())

        if(NewFields.issubset(RequiredFields)):
            """Creating Date From and To, sets date to current time"""
            NewData['date_from'] = date_from.strftime
            NewData['date_to'] = date_to.strftime
            datastore.create_item(NewData)

            """Assigns data to variables set by spec (bar NewId)"""
            user_id = NewData.get("user_id")
            keywords = NewData.get('keywords')
            description = NewData.get("description")
            lat = NewData.get("lat")
            lon = NewData.get("lon")
            newId = max(ITEMS.keys()) + 1

            """TODO: return date_from and date_to"""
            resp.media = {
                'id' : newId,
                'user_id' : user_id,
                'keywords' : NewData.get('keywords'),
                'description' : description,
                'lat' : lat,
                'lon' : lon,
            }
            resp.content_type = "application/json"
            """http.StatusCreated"""
            resp.status = falcon.HTTP_201
        else:
            """http.StatusMethodNotAllowed"""
            resp.status = falcon.HTTP_405
            resp.content_type = "application/json"
            print("POST /item","-", resp.status)
    
        """Old Delete code to refer"""
        #user_data = req.media
        #resp.media = {"id" : ITEMS.id, 'user_id' : ITEMS.user_id, 'description' : ""}
        #resp.status = falcon.HTTP_201
        #resp.content_type = falcon.MEDIA_JSON
        #fields = set(("user_id","keywords","description", "lat", "lon"))

        


          

"""adding new HTTP headers"""
class HandleCORSResource(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        

"""api routes"""

app = application = falcon.App(middleware=[HandleCORSResource()])
app.add_route('/item/{itemId}', GetResource())
app.add_route('/items', GetManyResource())
app.add_route('/item', PostResource())
app.add_route('/', RootResource())

"""Allan's cool code snippet, don't touch"""

if __name__ == '__main__':

    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8000, app)
    try:
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass