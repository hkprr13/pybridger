#-------------------------------------------------------------------------------
def oneToOne(relation: str):
    def decorator(cls):# -> Any:
        if not hasattr(cls, "__relations__"):
            setattr(cls, "__relations__", [])
        cls.__relations__.append(
            (cls.tableName, "o-o", relation)
        )
        return cls
    return decorator
#-------------------------------------------------------------------------------