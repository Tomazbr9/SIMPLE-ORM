from .fields import Field

from .registry import MODEL_REGISTRY

class MetaModel(type):
    def __new__(cls, name, bases, attrs):
    
        if name == 'ModelBase':
            return super().__new__(cls, name, bases, attrs)
        
        fields = {}
    
        for key, value in attrs.items():
            if isinstance(value, Field):
                value.name = key
                fields[key] = value
        
        attrs['_fields'] = fields
        
        new_class = super().__new__(cls, name, bases, attrs)
        MODEL_REGISTRY.append(new_class)

        return new_class

class ModelBase(metaclass=MetaModel):
    def __init__(self, **kwargs) -> None:
        for field_name in self._fields: # type: ignore
            setattr(self, field_name, kwargs.get(field_name))
    
    
    