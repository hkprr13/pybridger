#-------------------------------------------------------------------------------
from typing         import Any
from .GeometryType  import GeometryType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Polygon(GeometryType):
    """
    Define polygon type class
    Supported SQL (MySQL, PostgreSQL)
    """    
    def __init__(
            self,
            *coordinate : tuple[int | float, int | float]
        ) -> None:
        """
        Initialize path type object.
        Expressing polygons
        Args:
            coordinate : coordinate
        Examples:
            ```
            dataType = Polygon((0, 1), (2, 3), (4, 5), (6, 7), ...)
            ```
        """
        super().__init__()
        self.__coordinate = coordinate
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query(
            f"POLYGON{self.__coordinate}"
        )
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
            f"POLYGON{self.__coordinate}"
        )
#------------------------------------------------------------------------------