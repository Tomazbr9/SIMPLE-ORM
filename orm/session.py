from model import ModelBase
from query import QueryResult
from fields import Field

class Session:
    def __init__(self, engine) -> None:
        self._connection = engine
        self._engine = engine.cursor()

    def query(self, model):
        self.model = model
        return self
    
    def commit(self):
        self._connection.commit()
    
    def add(self) -> None:
    
        fields = self.model._fields  # type: ignore
        field_names = list(fields.keys())

        values = [getattr(self.model, field) for field in field_names]

        placeholders = ', '.join(['?'] * len(field_names))
        
        sql = f"""
            INSERT INTO {self.model.__class__.__name__.lower()} 
            ({', '.join(field_names)}) 
            VALUES ({placeholders})
        """
  
        self._engine.execute(sql, values)

    def get(self, id: int) -> QueryResult | None:
        self._engine.execute(
            f'SELECT * FROM {self.model.__name__} WHERE id = ?', (id,)
        )
        record = self._engine.fetchone()

        if not record:
            return None

        attribute_names = ['id'] + list(self.model._fields.keys()) # type: ignore
        
        data = dict(zip(attribute_names, record))
        return QueryResult(model_cls=self.model, data=data)
    


        

 
