from model import ModelBase

class Session:
    def __init__(self, engine) -> None:
        self._connection = engine
        self._engine = engine.cursor()

    def query(self, model: ModelBase):
        return self
    
    def commit(self):
        self._connection.commit()
    
    def add(self, model: ModelBase):
        new_records = model.__dict__

        keys = []
        values = []

        for i, j in new_records.items():

            keys.append(i)
            if isinstance(j, str):
                values.append(f'"{j}"')
                continue

            if isinstance(j, int):
                values.append(str(j))
                continue
            
            values.append(j)
        
        sql = f"""INSERT INTO {model.__class__.__name__} ({', '.join(keys)}) VALUES ({', '.join(values)})"""
        print(sql)
        self._engine.execute(sql)


        

 
