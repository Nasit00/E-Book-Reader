from abcItem import Item

class User(Item):
    def __init__(self, name, id):
        super().__init__(id)
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):      
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    @property
    def id(self):
        return self._id 
    @id.setter
    def id(self,value):
        if not isinstance(value,int) or value <= 0:
            raise ValueError("ID must be a positive integer")
        self._id = value
        
    def get_info(self):
        return f"User ID: {self.id}, Name: {self.name}"

    def __str__(self):
        return self.get_info()