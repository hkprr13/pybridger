#-------------------------------------------------------------------------------
from .Relation      import Relation
from ...model       import Model
#-------------------------------------------------------------------------------
class ManyToMany(Relation):
    def __init__(self, target : str) -> None:
        self.__target = target
    def __call__(self, cls : type[Model]) -> type[Model]:
        print("-----")
        print(cls.tableName)
        cls.__relation__.append(self.__target)
        print(cls.__foreignKey__)
        print(cls.__relation__)
        return cls
#-------------------------------------------------------------------------------