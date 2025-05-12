from model import ModelBase

class Session:
    def __init__(self, engine) -> None:
        self._engine = engine

    def query(self, model: ModelBase):
        return self
    
    def add(self, model: ModelBase):
        new_records = model.__dict__
        
        keys = []
        values = []

        for i, j in new_records.items():
            keys.append(i)
            values.append(j)
        
        sql = f"""INSERT INTO {model.__name__} ({', '.join(keys)}) VALUES ({', '.join(values)})"""
        self._engine.execute(sql)
        self._engine.commit()

        

 
