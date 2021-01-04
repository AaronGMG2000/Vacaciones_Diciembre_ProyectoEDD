import json 
from . import sha256 as sha
import os

class bloque:
    def __init__(self, numero, data, anterior, hashid):
        self.id = numero
        self.data = data
        self.anterior = anterior
        self.hash = hashid

    def get(self):
        return {"id":self.id, "content":self.data, "previous":self.anterior, "hash":self.hash}

class blockchain:
    def __init__(self):
        self.anterior = '0000000000000000000000000000000000000000000000000000000000000000'

    def crear(self, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps('', indent=4))
        file.close()

    def insertar(self, tablas, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        if type(lista)!=list:
            lista = []
        else:
            self.anterior = lista[-1]['hash']
        key = len(lista)
        key+=1
        values = ",".join(list(tablas.values()))
        id_hash = sha.generate(values)
        nuevo = bloque(key, tablas, self.anterior, id_hash)
        lista.append(nuevo.get())
        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps([j for j in lista], indent=4))
        self.anterior = id_hash

    def insert(self, data: list, database: str, table: str):
        dic = {}
        y=1
        for x in data:
            dic.update({y:x})
            y+=1
        self.insertar(dic, database, table)

    def update(self, tabla, registro, database, table, h2):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        for bloque in lista:
            if registro == bloque["hash"]:
                bloque["content"] = tabla
                bloque["hash"] = h2
        file = open("./Data/security/"+database+"_"+table+".json", "w+", encoding='utf-8')
        file.write(json.dumps(lista, indent=4))
        file.close()
    
    def CompararHash(self, data:list, newData: list, database, table):
        ldata = ",".join(str(x) for x in data)
        lnewData = ",".join(str(x) for x in newData)
        h1 = sha.generate(ldata)
        h2 = sha.generate(lnewData)
        dic = {}
        y=1
        for x in newData:
            dic.update({y:x})
            y+=1
        self.update(dic, h1, database, table, h2)
        if h1 == h2:
            return 0
        self.graficar(database, table)
        return 6
    
    def graficar(self, database, table):
        file = open("./Data/security/"+database+"_"+table+".json", "r")
        lista = json.loads(file.read())
        file.close()
        f= open('./Data/security/'+database+'_'+table+'.dot', 'w',encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box];\n')
        data =""
        t=0
        anterior = {}
        color = 'white'
        for x in lista:
            data = ''
            if len(anterior):
                if anterior['hash'] != x['previous']:
                    color = 'orangered'
            nombre = 'Nodo'+str(t)
            for y in list(x.values()):
                data+="""<tr><td>"""+str(y)+"""</td></tr>"""
            tabla ="""<<table BGCOLOR='"""+color+"""' cellspacing='0' cellpadding='20' border='0' cellborder='1'>
                """+data+"""        
            </table> >"""
            f.write(nombre+' [label = '+tabla+',  fontsize="30", shape = plaintext ];\n')
            t+=1
            anterior = x
        f.write('}')
        f.close()
        os.system('dot -Tpng ./Data/security/'+database+'_'+table+'.dot -o tupla.png')
        os.system('tupla.png')