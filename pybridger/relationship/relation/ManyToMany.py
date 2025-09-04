#-------------------------------------------------------------------------------
def manyToMany(relation: str):
    def decorator(cls):# -> Any:
        if not hasattr(cls, "__relations__"):
            setattr(cls, "__relations__", [])
        cls.__relations__.append(
            (cls.tableName, ">-<", relation)
        )
        return cls
    return decorator
#-------------------------------------------------------------------------------