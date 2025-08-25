#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase
#-------------------------------------------------------------------------------
class AsyncAlterTableAddConstraint(AsyncBase):
    def __init__(self, tableName: str) -> None:
        super().__init__(tableName)
#-------------------------------------------------------------------------------