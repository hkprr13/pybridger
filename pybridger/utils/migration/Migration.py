#-------------------------------------------------------------------------------
import os
import sys
import re
import hashlib
import importlib.util
from datetime       import datetime
from pathlib        import Path
from ...common      import private
from ...config      import Config
from ...mapper      import Query
#-------------------------------------------------------------------------------
class Migration:
    def __init__(
            self,
            migrationsDir : str
        ) -> None:
        """
        マイグレーションクラスの初期化
        Args:
            migrationsDir (str) : マイグレーションディレクトリのパス
        """
        super().__init__()
        self.__migrationsDir = Path(migrationsDir)
        self.__migrationsDir.mkdir(exist_ok = True)
        print("初期化完了")
    #---------------------------------------------------------------------------
    @property
    @private
    def __sqlEngine(self):# -> Any:
        """
        sqlエンジンの設定
        """
        engine = Config.sqlEngine
        if engine is None:
            raise Exception("エンジンが未設定です")
        return engine
    #---------------------------------------------------------------------------
    @property
    @private
    def __bulidHistoryQuery(self) -> Query:
        return Query("SELECT name FROM migration ORDER BY id")
    #---------------------------------------------------------------------------
    def make(self, name : str) -> None:
        """
        新しいマイグレーションファイルを作成する
        Args:
            name (str) : マイグレーション名
        """
        timeStamp = datetime.now().strftime("%Y%m%d%H%M%S")
        fileName  = f"{timeStamp}_" \
                  + f"{re.sub(r'[^0-9A-Za-z_]+', '_', name.strip())}.py"
        filePath  = os.path.join(self.__migrationsDir, fileName)
        with open(filePath, "w", encoding = "utf-8") as f:
            w = f.write
            w("def upgrade(engine):\n")
            w("    # ここにスキーマ変更SQLを記述\n")
            w("    pass\n")
            w("def downgrade(engine):\n")
            w("    # 元に戻すSQLを記述\n")
            w("    pass")
        print(f"{filePath}を作成しました")
    #---------------------------------------------------------------------------
    def history(self) -> list:
        """
        適用済みのマイグレーション一覧を返す
        Returns:
            list[str] : ファイル名のリスト
        """
        self.__sqlEngine.execute(self.__bulidHistoryQuery)
        rows = self.__sqlEngine.fetchall()
        if rows:
            return [r[0] for r in rows]
        else:
            return []
    
#-------------------------------------------------------------------------------