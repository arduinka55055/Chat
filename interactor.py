from object import Item
from typing import List


class Interactor:
    __items:List[Item]
    def loadDecorator(self,itemlist):
        self.__items=itemlist
    def getList(self):
        return self.__items
    def addItem(self,value:Item):
        self.__items.append(value)
        