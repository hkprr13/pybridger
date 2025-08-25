#-------------------------------------------------------------------------------
from ..Base         import Base  
from ...common      import private
#-------------------------------------------------------------------------------
class CreateTrigger(Base):
    """
    Define the trigger creation class
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            tableName   : str,
            triggerName : str,
            timing      : str,
            event       : str,
            body        : str
        ) -> None:
        """
        Initialize the trigger creation object
        Args:
            tableName   (str) : table name
            triggerName (str) : trigger name 
            timing      (str) : timing "BEFORE | AFTER"
            event       (str) : event  "INSERT | UPDATE | DELETE"
            body        (str) : query
        Examples:
            trigger = User.createTrigger(
                "tableName",
                "triggerName",
                "before | after",
                "inser | update | delete",
                query
            )
            trigger.execute()
            trigger.commit()
        """
        super().__init__(tableName)
        self.query = self.__buildQuery(
            tableName   = tableName,
            triggerName = triggerName,
            timing      = timing,
            event       = event,
            body        = body
        )
    #---------------------------------------------------------------------------
    @private
    def __buildQuery(
            self,
            tableName   : str,
            triggerName : str,
            timing      : str,
            event       : str,
            body        : str
        ) -> str:
        """
        Private method for creating trigger creation queries
        Initialize the trigger creation object
        Args:
            tableName   (str) : table name
            triggerName (str) : trigger name 
            timing      (str) : timing "before | after"
            event       (str) : event  "insert | update | delete"
            body        (str) : query
        """
        query = f"CREATE {triggerName} "
        if timing.lower() == "before":
            query += "BEFORE " # Space at the end
        elif timing.lower() == "after":
            query += "AFTER "  # Space at the end
        else:
            raise Exception(f"Specifying an invalid argument: {timing}")
        if event.lower() == "insert":
            query += "INSERT " # Space at the end
        elif event.lower() == "update":
            query += "UPDATE " # Space at the end
        elif event.lower() == "delete":
            query += "DELETE " # Space at the end
        else:
            raise Exception(f"Specifying an invalid argument: {event}")
        query += f"ON {tableName} EACH ROW BEGIN {body} END;"
        return query
#-------------------------------------------------------------------------------