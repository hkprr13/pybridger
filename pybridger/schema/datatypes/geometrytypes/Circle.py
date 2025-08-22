#-------------------------------------------------------------------------------
from typing         import Any
from .GeometryType  import GeometryType
from ....common     import override
from ....common     import private
from ....mapper     import Query
#-------------------------------------------------------------------------------
class Circle(GeometryType):
    """
    Define circle type class
    Supported SQL (PostgreSQL)
    """    
    def __init__(
            self,
            x : int | float , y : int | float, r : int | float
        ) -> None:
        """
        Initialize line type object.
        Used to represent a circle
        Args:
            x (int | float) : x coordinate
            y (int | float) : y coordinate
            r (int | float) : radius
        Examples:
            ```
            dataType = Circle(0, 10, 8)
            ```
        """
        super().__init__()
        self.x = x
        self.y = y
        self.r = r
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
            f"CIRCLE(({self.x, self.y}), {self.r})"
        )
#-------------------------------------------------------------------------------