from BplusTree4 import BPlusTree

class Table:

    def __init__(self, tabla = BPlusTree(5)):
        self.table = tabla
    
    def insert(self, register):
        if len(register)>self.table.columns:
            return 5
        else:
            reg = self.table.buscar(register)
            if reg:
                return 4
            else:
                self.table.register(register)
                return 0

    def loadCSV(self):
        pass

    def extractRow(self):
        pass
