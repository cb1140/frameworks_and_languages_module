import random
# array
ITEMS = {
    0: {
        "id": 0,
        "user_id": "user1234",
        "keywords": ["hammer", "nails", "tools"],
        "description": "A hammer and nails set",
        "lat": (random.random() * (70*2)) - 70, # Generating random Lat Lon as previous static data wasn't accurate
        "lon": (random.random() * (180*2)) - 180,
        "date_from": "2021-11-22T08:22:39.067408",
        "date_to": "2021-11-22T08:22:39.067408",

        
    }
}

# Dictionary to store items in 
class DataStorePythonDic():
    def __init__(self, items):
        self.items = items or {}
        self.items_id_max = max(self.items.keys() or (0,0))

    def get_item(self, id):
        return self.items.get(id)

    def delete_item(self, id):
        del self.items[id]
        
    def create_item(self, data):
        self.items_id_max +=1
        _id = self.items_id_max
        self.items[_id] = data
        data['id'] = _id
        return data

datastore = DataStorePythonDic(ITEMS)