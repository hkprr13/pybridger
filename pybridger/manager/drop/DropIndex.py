#-------------------------------------------------------------------------------
from ..Base     import Base    # 基底クラス
from ...common  import private # パブリックメソッド
from ...config  import Config  # コンフィグクラス
#-------------------------------------------------------------------------------
class DropIndex(Base):
    """インデックス削除クラス"""
    def __init__(
            self,
            tableName : str,
            indexName : str
        ):
        """
        インデックス削除クラスの初期化
        Args:
            tableName (str) : テーブル名
            indexName (str) : インデックス名
        """
        super().__init__(tableName)
        self.__indexName = indexName
        self.query = self.__buildQuery()
    #--------------------------------------------------------------------------
    def __buildQuery(self):
        """
        クエリの構築
        Returns:
            クエリ文字列
        Raises:
            Exceptin : エンジン未設定の場合
        """
        if self.sqlEngine == Config.sqlite3Engine:
            return f"DROP INDEX {self.__indexName};"
        elif self.sqlEngine == Config.MySqlEngine:
            return f"DROP INDEX {self.__indexName} ON {self.tableName};"
        else:
            raise Exception("エンジン未設定です")
#-------------------------------------------------------------------------------