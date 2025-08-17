#-------------------------------------------------------------------------------
from ...Base    import Base
from ....common import public
#-------------------------------------------------------------------------------
class CrossJoin(Base):
    #--------------------------------------------------------------------------
    def __init__(
            self,
            tableName : str,
            joinTable : str,            
        ):
        super().__init__(tableName)
        self.query = f"SELECT * FROM {tableName} "\
                   + f"CROSS JOIN {joinTable};"
#-------------------------------------------------------------------------------