#-------------------------------------------------------------------------------
from ..Base    import Base # 基底クラス
from ...common import public    # パブリックメソッド
#-------------------------------------------------------------------------------
class Where(Base):
    """WHEREクラス"""
    def __init__(
            self,
            tableName : str,
            columns   : str,
            condition : str,
            value     : tuple
        ):
        """
        WHEREクラスの初期化
            tableName (str)   : テーブル名
            columns   (str)   : カラム
            condition (str)   : 条件
            value     (tuple) : 値
        """
        super().__init__(tableName) 
        self.query = f"SELECT {columns} " \
                   + f"FROM {self.tableName} WHERE {condition};"
        self.value = value
    #---------------------------------------------------------------------------
    def inSubQuery(self, subQuery):
        query  = self.query[:-1]
        sQuery = subQuery[:-1]
        query += f" IN ({sQuery});"
        cur = self.sqlEngine.cursor()
        cur.execute(query, self.value)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def fetchall(self):
        """
        
        """
        cur = self.sqlEngine.cursor()
        cur.execute(self.query, self.value)
        return cur.fetchall()
#-------------------------------------------------------------------------------