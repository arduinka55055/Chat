from abc import ABCMeta, abstractmethod
from object import Item
from typing import List
from interactor import Interactor

class IDecorator(List[Item]) :
    __metaclass__ = ABCMeta
    @abstractmethod
    def send(self,data): raise NotImplementedError

    @abstractmethod
    def receive(self,data): raise NotImplementedError


class ConsoleDecorator(IDecorator):
    def send(self,data):
        print(data)
    def receive(self, data:Item):
        self.append(data)