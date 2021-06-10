from interactor import Interactor
from decorators import ConsoleDecorator
from object import Item, User
from typing import List


class Presenter:
    __items=Interactor()
    __items.loadDecorator(ConsoleDecorator())
    def addItem(self,text:str,name:str):
        item=Item()
        item.author=User()
        item.author.name=name
        item.text=text
        item.timestamp="10:06:2021"
        self.__items.addItem(item)
    def getItems(self):
        return self.__items.getList()
