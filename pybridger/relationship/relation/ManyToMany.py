#-------------------------------------------------------------------------------
from ...config      import Config
#-------------------------------------------------------------------------------
def manyToMany(relation: str):
    def decorator(cls):# -> Any:
        if not hasattr(cls, "__relations__"):
            setattr(cls, "__relations__", [])
        cls.__relations__.append(
            (cls.__tableName__, ">-<", relation)
        )
        Config.appendModelClasses(cls)
        return cls
    return decorator
#-------------------------------------------------------------------------------