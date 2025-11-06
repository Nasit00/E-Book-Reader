from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def get_info(self):
        pass