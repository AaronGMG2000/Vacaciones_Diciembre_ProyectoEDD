def loadCSV(filepath, database, table):
    if type(database) !=str or type(table)!=str or type(filepath)!=str:
        return []
    checkData()
    if validateIdentifier(database) and validateIdentifier(table):
        dataBaseTree = serializable.Read('./Data/', "Databases")
        root = dataBaseTree.getRoot()
        if not dataBaseTree.search(root, database.upper()):
            return []
        tablesTree = serializable.Read(f"./Data/{database}/", database)
        if not tablesTree.search(tablesTree.getRoot(), table.upper()):
            return []
        try:
            res = []
            import csv
            PKsTree = serializable.Read(f'./Data/{database}/{table}/', table)
            with open(filepath, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    res.append(PKsTree.register(row))
            serializable.update(f'./Data/{database}/{table}/', table, PKsTree)
            return res
        except:
            return []
    else:
        return []