from .registry import MODEL_REGISTRY

def create_all_tables(engine):
    for model in MODEL_REGISTRY:
        field_sqls = []

        for field in model._fields.values():
            field_sqls.append(field.get_sql())

        sql = f"""
            CREATE TABLE IF NOT EXISTS {model.__name__.lower()}(
                {','.join(field_sqls)}
            )
            """
        engine.execute(sql)