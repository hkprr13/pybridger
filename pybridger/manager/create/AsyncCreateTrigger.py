#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase # 基底クラス
from ...common   import private   # プライベートメソッド
from ...common   import public    # パブリックメソッド
#-------------------------------------------------------------------------------
class AsyncCreateTrigger(AsyncBase):
    """
    Definition of the class for creating asynchronous triggers
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
        Initializing the asynchronous trigger creation class
        Args:
            tableName   (str) : Table name
            triggerName (str) : Trigger name 
            timing      (str) : Timing "BEFORE | AFTER"
            event       (str) : Event  "INSERT | UPDATE | DELETE"
            body        (str) : Query to execute
        Examples:
            ```
            trigger = User.createTrigger(
                "tableName",
                "triggerName",
                "before | after",
                "inser | update | delete",
                "query"
            )
            trigger.execute()
            trigger.commit()
            ```
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
        Args:
            tableName   (str) : Table name
            triggerName (str) : Trigger name 
            timing      (str) : Timing "BEFORE | AFTER"
            event       (str) : Event  "INSERT | UPDATE | DELETE"
            body        (str) : Query to execute
        """
        query = f"CREATE TRIGGER {triggerName} "
        if timing.lower() == "before":
            query += "BEFORE " # Space at the end
        elif timing.lower()  == "after":
            query += "AFTER "  # Space at the end
        else:
            raise Exception(f"Specifying an invalid argument: {timing}")
        if event.lower()  == "insert":
            query += "INSERT " # Space at the end
        elif event.lower()  == "update":
            query += "UPDATE " # Space at the end
        elif event.lower()  == "delete":
            query += "DELETE " # Space at the end
        else:
            raise Exception(f"Specifying an invalid argument: {event}")
        query += f"ON {tableName} EACH ROW BEGIN {body} END;"
        return query
#-------------------------------------------------------------------------------