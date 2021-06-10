import json
class User:
    name:str

class Item:
    text:str
    timestamp:str
    author:User
    def toDict(self):
        return {"msg":self.author.name+" : "+self.text}
    def toJSON(self):
        return json.dumps(self.toDict())