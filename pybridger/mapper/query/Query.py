#-------------------------------------------------------------------------------
class Query:
    """
    Define Query class
    """
    def __init__(self, value : object) -> None:
        """
        Initialize query object
        Args:
            value (object): query
        """
        self.__value = value
    #---------------------------------------------------------------------------
    @property
    def sql(self) -> str:
        return str(self.__value)
#-------------------------------------------------------------------------------