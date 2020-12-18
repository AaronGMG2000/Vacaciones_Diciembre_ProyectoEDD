import AVLTree
import BplusTree
import os
import pickle
import Serializable as serializable
import re
import shutil


def dropAll():
    if os.path.isdir('./Data'):
        shutil.rmtree('./Data')


def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Databases.bin"):
        with open("./Data/Databases.bin", 'wb') as f:
            dataBaseTree = AVLTree.AVLTree()
            pickle.dump(dataBaseTree, f)


# Checks if the name is a valid SQL Identifier
def validateIdentifier(identifier):
    # Returns true if is valid
    return not re.search(r"[^a-zA-Z0-9 ]+|^[\s]", identifier)


def createDatabase(database):
    checkData()
    if database and validateIdentifier(database):
        dataBaseTree = serializable.Read('./Data/', 'Databases')
        root = dataBaseTree.getRoot()
        if dataBaseTree.search(root, database):
            return 2
        else:
            dataBaseTree.add(root, database)
            serializable.write('./Data/', database, AVLTree.AVLTree())
            serializable.update('./Data/', 'Databases', dataBaseTree)
        return 0
    else:
        return 1


def showDatabases():
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    dbKeys = dataBaseTree.postOrder(root)
    return [] if len(dbKeys) == 0 else dbKeys[:-1].split("-")


def alterDatabase(dataBaseOld, dataBaseNew) -> int:
    checkData()
    if validateIdentifier(dataBaseOld) and validateIdentifier(dataBaseNew):
        dataBaseTree = serializable.Read('./Data/', "Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, dataBaseOld):
            return 2
        if dataBaseTree.search(root, dataBaseNew):
            return 3
        dataBaseTree.delete(root, dataBaseOld)
        serializable.Rename('./Data/', dataBaseOld, dataBaseNew)
        dataBaseTree.add(root, dataBaseNew)
        serializable.update('./Data/', 'Databases', dataBaseTree)
        return 0
    else:
        return 1


def dropDatabase(database):
    checkData()
    if validateIdentifier(database):
        dataBaseTree = serializable.Read('./Data/', "Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, database):
            return 2
        dataBaseTree.delete(root, database)
        serializable.delete('./Data/' + database)
        serializable.update('./Data/', 'Databases', dataBaseTree)
        return 0
    else:
        return 1


# ---------------CRUD TABLE----------------#
# ----------------Erick--------------------#

def createTable(database, table, numberColumns):
    # Validates identifier before searching
    if validateIdentifier(database) and validateIdentifier(table) and numberColumns >= 0:
        checkData()
        # Get the databases tree
        dataBaseTree = serializable.Read('./Data/', "Databases")
        # Get the dbNode
        databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
        # If DB exist
        if databaseNode:
            tablesTree = serializable.Read(f"./Data/{database}/", database)
            if tablesTree.search(tablesTree.getRoot(), table):
                return 3
            else:
                # Creates new table node
                tablesTree.add(tablesTree.getRoot(), table)
                serializable.update(f"./Data/{database}/", database, tablesTree)
                # Creates bin file for the new table
                serializable.write(f"./Data/{database}/", table, BplusTree.BPlusTree(5, numberColumns))
                return 0
        else:
            return 2
    else:
        return 1


def showTables(database):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    dataBaseTree.search(dataBaseTree.getRoot(), database)
    if dataBaseTree.search(dataBaseTree.getRoot(), database):
        db = serializable.Read(f"./Data/{database}/", database)
        dbKeys = db.postOrder(db.getRoot())
        return [] if len(dbKeys) == 0 else dbKeys[:-1].split("-")
    else:
        return None


def extractTable(database, table):
    checkData()
    # Get the databases tree
    dataBaseTree = serializable.Read('./Data/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
    # If DB exist
    if databaseNode:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table):
            table = serializable.Read(f'./Data/{database}/{table}/', table)
            return list(table.lista().values())
        else:
            return None
    else:
        return None


def extractRangeTable(database, table, columnNumber, lower, upper):
    checkData()
    # Get the databases tree
    dataBaseTree = serializable.Read('./Data/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
    # If DB exist
    if databaseNode:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table):
            table = serializable.Read(f'./Data/{database}/{table}/', table)
            tableList = list(table.lista().values())
            validList = []

            if columnNumber < 0 or columnNumber >= len(tableList):
                return None

            for i in tableList:
                if str(i[columnNumber]) <= str(upper) and str(i[columnNumber]) >= str(lower):
                    validList.append(i)
            return validList

        else:
            return None
    else:
        return None


# ---------------Dyllan--------------------#

def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        checkData()
        # Get the databases tree
        dataBaseTree = serializable.Read('./Data/', "Databases")
        # Get the dbNode
        databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
        # If DB exist
        if databaseNode:
            tablesTree = serializable.Read(f"./Data/{database}/", database)
            if not tablesTree.search(tablesTree.getRoot(), table):
                return 3  # table no existente
            else:
                tuplaTree = serializable.Read(f"./Data/{database}/{table}/", table)
                maximun = max(columns)
                minimun = min(columns)
                numberColumnsA = tuplaTree.columns  # actual amount from column
                if not (minimun >= 0 and maximun < numberColumnsA):
                    return 5
                res = tuplaTree.CreatePK(columns)
                if res:
                    return res
                else:
                    serializable.update(f"./Data/{database}/{table}/", table, tuplaTree)
                    return 0
        else:
            return 2  # database no existente
    except:
        return 1


def alterDropPK(database: str, table: str) -> int:
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        return 2  # database no existente
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            return 3  # table no existente

        PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
        res = PKsTree.DeletePk()
        if res:
            return res
        else:
            serializable.update(f'./Data/{database}/{table}/', table, PKsTree)
        return 0  # exito


# ---------------CRUD TUPLA----------------#
# ---------------Rudy----------------------#
def insert(database, table, register):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        return 2  # database no existente
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            return 3  # table no existente
        PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
        if PKsTree.buscar(register):
            return 4
        res = PKsTree.register(register)
        if res:
            return res
        serializable.update(f'./Data/{database}/{table}/', table, PKsTree)
        return 0  # exito


def loadCSV(filepath, database, table):
    checkData()
    col = False
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        if createDatabase(database):
            return []
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            col = True
        try:
            res = []
            import csv
            with open(filepath, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    if col:
                        if createTable(database, table, len(row)):
                            return []
                        col = False
                    res.append(insert(database, table, row))
            return res
        except:
            return []


def extractRow(database, table, columns):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        return []  # database no existente
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            return []  # table no existente
        PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
        return PKsTree.search(columns)  # exito


def update(database, table, register, columns):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        return 2  # database no existente
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            return 3  # table no existente
        PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
        try:
            res = PKsTree.update(register, columns)
            serializable.update(f'./Data/{database}/{table}/', table, PKsTree)
            return res
        except:
            return 1


def delete(database, table, columns):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        return 2  # database no existente
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            return 3  # table no existente
        PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
        if len(PKsTree.search(columns)):
            try:
                PKsTree.delete(columns)
                serializable.update(f'./Data/{database}/{table}/', table, PKsTree)
                return 0
            except:
                return 1
        else:
            return 4


def truncate(database, table):
    checkData()
    dataBaseTree = serializable.Read('./Data/', "Databases")
    root = dataBaseTree.getRoot()
    if not dataBaseTree.search(root, database):
        return 2  # database no existente
    else:
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table):
            return 3  # table no existente
        PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
        try:
            PKsTree.trunate()
            serializable.update(f'./Data/{database}/{table}/', table, PKsTree)
            return 0
        except:
            return 1

# ---------------Marcos--------------------#
# ***************Pruebas*******************#
# *---------------Rudy--------------------*#
# *---------------Marcos------------------*#
# *---------------Erick-------------------*#
# *--------------Dyllan-------------------*#
