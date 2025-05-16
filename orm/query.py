from model import ModelBase

class QueryResult:
    def __init__(self, model_cls: ModelBase, data: dict) -> None:
        self.model_cls = model_cls
        self.__dict__.update(data)
    
    def __repr__(self) -> str:
        return f'<QueryResult{self.model_cls.__name__} {self.__dict__}>'