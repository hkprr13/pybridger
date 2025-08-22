#-------------------------------------------------------------------------------
from typing         import Any
from .GeometryType  import GeometryType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Point(GeometryType):
    """
    Define point type class
    Supported SQL (PostgreSQL)
    """    
    def __init__(
            self,
            x : int | float , y : int | float
        ) -> None:
        """
        Initialize point type object.
        Representing a specific location on a map
        Args:
            x (int | float) : x coordinate
            y (int | float) : y coordinate
        Examples:
            ```
            dataType = Point(3, 4)
            ```
        """
        super().__init__()
        self.x = x
        self.y = y
    #---------------------------------------------------------------------------
    @override
    @private
    def mysql(self) -> None:
        self.query : Any = Query(
            f"POINT({self.x, self.y})"
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
            f"POINT({self.x, self.y})"
        )
#-------------------------------------------------------------------------------