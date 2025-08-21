#-------------------------------------------------------------------------------
from .Constraints   import Constraints  # 基底クラス
from ...common      import override     # オーバライドデコレーター
from ...common      import public       # パブリックデコレーター
from ...mapper      import Query        # クエリクラス
#-------------------------------------------------------------------------------
class PrimaryKey(Constraints):
    """
    主キー制約クラス
    """
    #---------------------------------------------------------------------------
    @public
    def __buildPrimaryKeyQuery(self) -> Query:
        """
        主キー制約の定義
        Returns:
            Query : PRIMARY KEYのクエリを返す
        """
        return Query("PRIMARY KEY")
    #---------------------------------------------------------------------------
    @override
    def mysql(self) -> None:
        self.query  = self.__buildPrimaryKeyQuery()
    #---------------------------------------------------------------------------
    @override
    def sqlite3(self) -> None:
        self.query  = self.__buildPrimaryKeyQuery()
    #---------------------------------------------------------------------------
    @override
    def postgresql(self) -> None:
        self.query  = self.__buildPrimaryKeyQuery()
#-------------------------------------------------------------------------------
