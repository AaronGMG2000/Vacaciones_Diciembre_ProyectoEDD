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
                serializable.write(f"./Data/{database}/", table, BplusTree.BPlusTree(5,numberColumns))
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
                return 3 # table no existente
            else:
                tuplaTree = serializable.Read(f"./Data/{database}/{table}/", table)
                maximun = max(columns)
                minimun = min(columns)
                numberColumnsA = tuplaTree.columns  #actual amount from column
                if not (minimun>=0 and maximun<numberColumnsA):
                    return 5
                res = tuplaTree.CreatePK(columns)
                if res:
                    return res
                else:
                    serializable.update(f"./Data/{database}/{table}/", table, tuplaTree)
                    return 0
        else:
            return 2 #database no existente
    except:
        return 1  

def alterDropPK(database: str, table: str) -> int:

    checkData()
    if validateIdentifier(database):
        dataBaseTree = serializable.Read('./Data/', "Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, database):
            return 2 #database no existente
        else:
            tablesTree = serializable.Read(f"./Data/{database}/", database)
            if not tablesTree.search(tablesTree.getRoot(), table):
                return 3 # table no existente
            
            PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
            res = PKsTree.DeletePk()
            if res:
                return res
            else:
                serializable.update(f'./Data/{database}/{table}/',table , PKsTree)
            return 0 # exito
    else:
        return 1  #error

# ---------------CRUD TUPLA----------------#
# ---------------Rudy----------------------#
# ---------------Marcos--------------------#
# ***************Pruebas*******************#
# *---------------Rudy--------------------*#
# *---------------Marcos------------------*#
# *---------------Erick-------------------*#
# *--------------Dyllan-------------------*#
