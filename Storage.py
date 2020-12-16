import AVLTree
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
            serializable.write('./Data/',database,AVLTree.AVLTree())
            serializable.update('./Data/','Databases', dataBaseTree)
        return 0
    else:
        return 1


def showDatabases():
    checkData()
    dataBaseTree = serializable.Read('./Data/',"Databases")
    root = dataBaseTree.getRoot()
    dbKeys = dataBaseTree.postOrder(root)
    dataBaseTree.graph()
    return dbKeys[:-1].split("-")


def alterDatabase(dataBaseOld, dataBaseNew) -> int:
    checkData()
    if validateIdentifier(dataBaseOld) and validateIdentifier(dataBaseNew):
        dataBaseTree = serializable.Read('./Data/',"Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, dataBaseOld):
            return 2
        if dataBaseTree.search(root, dataBaseNew):
            return 3
        dataBaseTree.delete(root, dataBaseOld)
        serializable.Rename('./Data/',dataBaseOld,dataBaseNew)
        dataBaseTree.add(root, dataBaseNew)
        serializable.update('./Data/','Databases', dataBaseTree)
        return 0
    else:
        return 1

def dropDatabase(database):
    checkData()
    if validateIdentifier(database):
        dataBaseTree = serializable.Read('./Data/',"Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, database):
            return 2
        dataBaseTree.delete(root, database)
        serializable.delete('./Data/'+database)
        serializable.update('./Data/','Databases', dataBaseTree)
        return 0
    else:
        return 1
#---------------CRUD TABLE----------------#
#----------------Erick--------------------#
#---------------Dyllan--------------------#
#---------------CRUD TUPLA----------------#
#---------------Rudy----------------------#
#---------------Marcos--------------------#
#***************Pruebas*******************#
#*---------------Rudy--------------------*#
#*---------------Marcos------------------*#
#*---------------Erick-------------------*#
#*--------------Dyllan-------------------*#
