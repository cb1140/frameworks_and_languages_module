ITEMS = {}

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