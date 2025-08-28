#-------------------------------------------------------------------------------
from typing         import Any
from .Relation      import Relation
from ...model       import Model
#-------------------------------------------------------------------------------
class OneToOne(Relation):
    def __init__(self, target : str) -> None:
        self.__target = target
    def __call__(self, cls : type[Model]) -> type[Model]:
        print("OneToOne")
        print(cls.tableName)
        print(cls.columns)
        return cls
#-------------------------------------------------------------------------------