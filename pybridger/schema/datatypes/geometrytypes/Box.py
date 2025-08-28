#-------------------------------------------------------------------------------
from typing         import Any
from .GeometryType  import GeometryType
from ....common     import override
from ....common     import public
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Box(GeometryType):
    """
    Define box type class
    Supported SQL (PostgreSQL)
    """    
    def __init__(
            self,
            x1 : int | float , y1 : int | float,
            x2 : int | float , y2 : int | float
        ) -> None:
        """
        Initialize box type object.
        Used to represent rectangles
        Args:
            x1 (int) : x1 coordinate
            y1 (int) : y1 coordinate
            x2 (int) : x2 coordinate
            y2 (int) : y2 coordinate
        Examples:
            ```
            dataType = Box(0, 4, 10, 12)
            ```
        """
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    #---------------------------------------------------------------------------
    @override
    @public
    def mysql(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @public
    def sqlite3(self) -> None:
        self.query : Any = self.TEXTNOTSUPPORTED
    #---------------------------------------------------------------------------
    @override
    @public
    def postgresql(self) -> None:
        self.query : Any = Query(
            f"Box(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"
        )
#-------------------------------------------------------------------------------