#-------------------------------------------------------------------------------
def oneToMany(relation: str):
    def decorator(cls):# -> Any:
        if not hasattr(cls, "__relations__"):
            setattr(cls, "__relations__", [])
        cls.__relations__.append(
            (cls.tableName, "o-<", relation)
        )
        return cls
    return decorator
#-------------------------------------------------------------------------------