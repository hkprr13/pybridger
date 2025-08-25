#-------------------------------------------------------------------------------
import csv
from typing import Any
from ...common      import private 
from ...common      import public
from ...config      import Config
from ..column       import Column
from ..conditions   import Condition 
from ...mapper      import Query
from ...errors      import EngineUndefinedError
#-------------------------------------------------------------------------------
class View:
    """
    Define view class
    """
    #---------------------------------------------------------------------------
    def __init__(
            self,
            viewName   : str,
            conditions : Condition,
            *columns   : Column
        ) -> None:
        """
        Initialize view object
        Arguments:
            viewName   (str)       : View name
            conditions (Condition) : Condition User.age >= 20
            *columns   (Column)    : Column
        Examples:
            view = View(“viewName”, User.age >= 20, User.id, User.name)
        """
        self.__viewName   = viewName
        self.__conditions = conditions
        self.__columns    = columns
    #---------------------------------------------------------------------------
    @property
    @private
    def __sqlEngine(self) -> Any:
        """
        Setting SQL engine
        """
        engine = Config.sqlEngine
        if engine is None:
            raise EngineUndefinedError()
        return engine
    #---------------------------------------------------------------------------
    @ private
    def __bulidSelectQuery(self) -> str:
        query     = "SELECT " 
        tableName = ""
        for col in self.__columns:
            tableName = col.tableName
            query += f"{col.columnName}, "
        else:

            query = query[:-2]
            query += f" FROM {tableName} WHERE {self.__conditions}"
        # SELECT id, name FROM User WHERE age >= 10
        return query
    #---------------------------------------------------------------------------
    @public
    def create(
            self,
            replace             : bool = False,
            checkOption         : bool = False,
            localCheckOption    : bool = False,
            cascadedCheckOption : bool = False,
            securityDefiner     : bool = False,
            readOnly            : bool = False
        ) -> None:
        """
        Create a view in the database. No output
        Args:
            replace             (bool) : Replace existing view.
            checkOption         (bool) : Restrict updates through view.
            localCheckOption    (bool) : Enforce only own conditions in nested views.
            cascadedCheckOption (bool) : Enforce all conditions in nested views.
            securityDefiner     (bool) : Execute with the permissions of the user who created the view
            readOnly            (bool) : Prohibit write operations from the view
        Examples:
            view = View(“viewName”, User.age >= 10, User.id, User.name)
            view.create(replece = True, checkOption = True)
        """
        query     = f"CREATE "
        selectSql = self.__bulidSelectQuery()
        if replace == True:
            query += "OR REPLACE "
        # CREATE VIEW viewName AS SELECT id, name FROM User WHERE age >= 10
        query += f"VIEW {self.__viewName} AS {selectSql} " 
        # オプション句の構築
        withClauses = []
        if checkOption:
            withClauses.append("CHECK OPTION")
        if localCheckOption:
            withClauses.append("LOCAL CHECK OPTION")
        if cascadedCheckOption:
            withClauses.append("CASCADED CHECK OPTION")
        if securityDefiner:
            withClauses.append("SECURITY DEFINER")
        if readOnly:
            withClauses.append("READ ONLY")
        if withClauses:
            query += f"WITH {' '.join(withClauses)}"
            query += ";"
        else:
            query = query[:-1] + ";" 
        self.__sqlEngine.execute(query = Query(query))
        self.__sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    def show(self) -> list:
        """
        Display view
        Returns:
            Returns a view iterator.
        """
        query = f"SELECT * FROM {self.__viewName};"
        cur = self.__sqlEngine.cursor()
        cur.execute(query)
        return cur.fetchall()
    #---------------------------------------------------------------------------
    @public
    def drop(self) -> None:
        """
        Delete view
        """
        query = f"DROP VIEW IF EXISTS {self.__viewName};"
        self.__sqlEngine.execute(query = Query(query))
        self.__sqlEngine.commit()
    #---------------------------------------------------------------------------
    @public
    def makeCSV(
            self,
            filePath      : str,
            includeHeader : bool = True,
            encoding      : str = "utf-8"
        ) -> None:
        """
        Output view contents as a CSV file.
        Args:
            filePath      (str)  : Output CSV file path (.csv not required)
            includeHeader (bool) : Whether to include header row (column names) in output
            encoding       (str)  : Output file character encoding
        Raises:
            Exception : When engine is not set or query fails
        """
        cur = self.__sqlEngine.cursor()
        cur.execute(f"SELECT * FROM {self.__viewName};") # ビュー名で指定
        if cur.description is None:
            print("Output failed")
            return
        columnNames = [description[0] for description in cur.description]
        rows = cur.fetchall()
        try:
            with open(
                file    = f"{filePath}.csv", mode     = "w",
                newline = "",                encoding = encoding
            ) as f:
                writer = csv.writer(f)
                if includeHeader:
                    writer.writerow(columnNames)
                writer.writerows(rows) 
            print("Output successful")
        except Exception as e:
            print(e)            
#-------------------------------------------------------------------------------