from abc import ABC, abstractmethod

class Field(ABC):

    def __init__(self, name=None, primary_key=False, null=True) -> None:
        self.name = name
        self.primary_key = primary_key
        self.null = null

    @abstractmethod
    def get_sql(self):
        ...

class StringField(Field):
    def __init__(self, name=None, primary_key=False, null=True, max_length=255) -> None:
        super().__init__(name, primary_key, null)
        self.max_length = max_length
    
    def get_sql(self):
        if self.null:
            return f'{self.name} VARCHAR({self.max_length})'
        return f'{self.name} VARCHAR({self.max_length}) NOT NULL'


class IntegerField(Field):
    
    def get_sql(self):
        if self.primary_key:
            return f'{self.name} INTEGER PRIMARY KEY AUTOINCREMENT'
        
        if self.null:
            return f'{self.name} INTEGER '
        
        return f'{self.name} INTEGER NOT NULL'

class DecimalField(Field):
    ...

class BoolField(Field):
    ...