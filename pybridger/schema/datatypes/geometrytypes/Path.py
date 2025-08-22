#-------------------------------------------------------------------------------
from typing         import Any
from .GeometryType  import GeometryType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Path(GeometryType):
    """
    Define path type class
    Supported SQL (PostgreSQL)
    """    
    def __init__(
            self,
            *coordinate : tuple[int | float, int | float]
        ) -> None:
        """
        Initialize path type object.
        Expressing closed polygonal paths/ Expressing open path paths
        Args:
            coordinate : coordinate
        Examples:
            ```
            dataType = Path((0, 1), (2, 3), (4, 5), (6, 7), ...)
            ```
        """
        super().__init__()
        self.__coordinate = coordinate
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def sqlite3(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @private
    def postgresql(self) -> None:
        self.query : Any = Query(
            f"Path{self.__coordinate}"
        )
#-------------------------------------------------------------------------------