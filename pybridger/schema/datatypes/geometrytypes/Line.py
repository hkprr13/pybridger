#-------------------------------------------------------------------------------
from typing         import Any
from .GeometryType  import GeometryType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Line(GeometryType):
    """
    Define line type class
    Supported SQL (PostgreSQL)
    """    
    def __init__(
            self,
            x1 : int | float , y1 : int | float,
            x2 : int | float , y2 : int | float
        ) -> None:
        """
        Initialize line type object.
        Expressing an infinitely extending straight line
        Args:
            x1 (int | float) : x1 coordinate
            y1 (int | float) : y1 coordinate
            x2 (int | float) : x2 coordinate
            y2 (int | float) : y2 coordinate
        Examples:
            ```
            dataType = Line(0, 4, 10, 12)
            ```
        """
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
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
            f"Line(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"
        )
#-------------------------------------------------------------------------------