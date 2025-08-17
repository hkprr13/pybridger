#-------------------------------------------------------------------------------
from ..AsyncBase import AsyncBase # 基底クラス
from ...common   import public    # パブリックメソッド
#-------------------------------------------------------------------------------
class AsyncCreateIndex(AsyncBase):
    """非同期インデックス作成クラス"""
    def __init__(
            self,
            indexName : str,
            tableName : str,
            columns   : str
        ):
        """
        非同期インデックス作成クラスの初期化
        Args:
            indexName (str) : インデックス名
            tableName (str) : テーブル名
            columns   (str) : カラム
        """
        super().__init__(tableName)
        self.query = f"CREATE {indexName} ON {tableName} ({columns});"
#-------------------------------------------------------------------------------