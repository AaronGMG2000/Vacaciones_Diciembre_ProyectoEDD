import AVLTree
import os
import pickle
import re


def checkData():
    if not os.path.isdir("./Data"):
        os.mkdir("./Data")
    if not os.path.isfile("./Data/Databases.bin"):
        with open('./Data/Databases.bin', 'wb') as f:
            dataBaseTree = AVLTree.AVLTree()
            pickle.dump(dataBaseTree, f)


def createDatabase(database):
    checkData()
    if database and not re.match(r"[^a-zA-Z0-9 ]|^[\s]", database):
        with open("./Data/Databases.bin", "rb") as f:
            dataBaseTree = pickle.load(f)
            root = dataBaseTree.getRoot()
            if dataBaseTree.search(root, database):
                return 2
            else:
                dataBaseTree.add(root, database)
        with open("./Data/Databases.bin", "wb") as f:
            pickle.dump(dataBaseTree, f)
        return 0
    else:
        return 1


def showDatabases():
    checkData()
    with open("./Data/Databases.bin", "rb") as f:
        dataBaseTree = pickle.load(f)
        root = dataBaseTree.getRoot()
        dbKeys = dataBaseTree.postOrder(root)
        return dbKeys[:-1].split("-")




print(createDatabase("   Queso"))
print(createDatabase("_#B"))
print(createDatabase("@Casa"))
print(createDatabase("_Zanahoria"))
print(createDatabase("$Z"))
print(createDatabase("Base1"))
print(createDatabase("Base datos 2"))
print(createDatabase("Base1"))

print(showDatabases())
