#-------------------------------------------------------------------------------
from .Constraints   import Constraints  # 基底クラス
from ...common      import override     # オーバライドデコレーター
from ...mapper      import Query        # クエリクラス
#-------------------------------------------------------------------------------
class Check(Constraints):
    """
    Defined check constraints
    """
    def __init__(self, conditons : str) -> None:
        """
        Initialize check constraints object
        Args:
            condtions (str) : conditional expression by specify string
        """
        self.__conditions = conditons
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = Query(f"CHECK ({self.__conditions})")
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = Query(f"CHECK ({self.__conditions})")
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = Query(f"CHECK ({self.__conditions})")
#-------------------------------------------------------------------------------