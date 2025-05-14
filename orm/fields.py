from abc import ABC, abstractmethod

class Field(ABC):

    def __init__(self, name: str | None = None, null: bool = True) -> None:
        self.name = name
        self.null = null

    @abstractmethod
    def get_sql(self):
        ...

class StringField(Field):
    def __init__(self, name=None, null=True, max_length=255) -> None:
        super().__init__(name, null)
        self.max_length = max_length
    
    def get_sql(self):
        if self.null:
            return f'{self.name} VARCHAR({self.max_length})'
        return f'{self.name} VARCHAR({self.max_length}) NOT NULL'


class IntegerField(Field):
    
    def get_sql(self):
        
        if self.null:
            return f'{self.name} INTEGER '
        
        return f'{self.name} INTEGER NOT NULL'

class DecimalField(Field):
    ...

class BoolField(Field):
    ...