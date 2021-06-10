from presenter import Presenter


class Router(Presenter):
    def request(self,data,username):
        if not username==None:
            self.addItem(data, username)
        else:
            self.addItem(data, "анонимус")
    def response(self):
        return self.getItems()[-1].toDict()
    def hello(self,username):
        if not username==None:
            self.addItem("Только что присоденился к чату!", username)
    def bye(self,username):
        if not username==None:
            self.addItem(" Только что покинул комнату.....Жаль:(", username)