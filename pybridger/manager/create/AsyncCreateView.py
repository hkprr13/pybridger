#-------------------------------------------------------------------------------
from ..Base    import Base  
from ...common import public 
#-------------------------------------------------------------------------------
class AsyncCreateView(Base):
    def __init__(
            self,
            viewName  : str,
            tableName : str,
            columns   : str
        ) -> None:
        super().__init__(tableName)
        self.__viewName  = viewName
        self.__columns   = columns
    #---------------------------------------------------------------------------
    @public
    async def where(self, **conditon):
        query = f"CREATE VIEW {self.__viewName} AS"
        con = ""
        for key, value in conditon.items():
            con += f"{key} = {value}"
        return ...
#-------------------------------------------------------------------------------