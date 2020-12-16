import os
import random

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.keys = []
        self.values = {}
        self.child = []
        self.next = None
        self.leaf = True
    
    def insert(self, key, value):
        self.keys.append(key)
        if value:
            self.values[key] = value
        if len(self.keys) > 1:
            self.keys.sort()
class BPlusTree:

    def __init__(self, degree = 5):
        self.root = Node(None)
        self.degree = degree
        self.valuar = False
        self.PKey = []
        self.Fkey = []
        self.Incremet = 1
        self.columns = 0

    def insert(self, key, value):
        if key == 0:
            print("")
        self.root = self._insert(self.root, str(key), value)
        self.valuar = False
    
    def _insert(self, temp, key, value):
        if temp.leaf:
            if key not in temp.keys:
                temp.insert(key, value)
            else:
                return temp
        else:
            found = False
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    found = True
                    self._insert(temp.child[i], key, value)
                    break
            if not found:
                self._insert(temp.child[len(temp.keys)], key, value)

        if len(temp.keys) == self.degree:
            if temp.parent == None:
                c = temp
                temp = Node(None)
                temp.insert(c.keys[int((self.degree)/2)], None)
                temp.child.append(Node(temp))
                temp.child.append(Node(temp))
                if self.valuar:
                    temp.child[0].keys = c.keys[0:int((self.degree)/2)]
                    temp.child[1].keys = c.keys[int((self.degree)/2)+1:]
                    # k = 0
                    if self.degree%2 == 0:
                        ii = int((len(c.child))/2)+1
                    else:
                        ii = int((len(c.child))/2)
                    for i in range(0,ii):
                        c.child[i].parent = temp.child[0]
                        temp.child[0].child.append(c.child[i])
                    for i in range(ii, len(c.child)):
                        c.child[i].parent = temp.child[1]
                        temp.child[1].child.append(c.child[i])
                    temp.child[0].leaf = False
                    temp.child[1].leaf = False
                    self.valuar=False
                else:
                    temp.child[0].keys = c.keys[0:int((self.degree)/2)]
                    temp.child[1].keys = c.keys[int((self.degree)/2):]
                    if temp.leaf:
                        temp.child[0].next = temp.child[1]
                        temp.child[1].next = c.next
                if len(c.values):
                    for x in temp.child[1].keys:
                        temp.child[1].values[x] = c.values.get(x)
                    for x in temp.child[0].keys:
                        temp.child[0].values[x] = c.values.get(x)
                temp.leaf = False
            else:
                n = 0
                ev = False
                v = temp.values
                if self.valuar:
                        n = 1
                        ev = True
                        self.valuar = False
                mkey = temp.keys[int((self.degree)/2)]
                temp.parent.insert(str(mkey), None)
                index = 0
                for index in range(0, len(temp.parent.keys)):
                    if temp.parent.keys[index] == mkey:
                        break
                temp.parent.child.append(Node(temp))
                if index+1 < len(temp.parent.child):
                    k = len(temp.parent.child)-1
                    while k > index:
                        temp.parent.child[k] = temp.parent.child[k-1]
                        k-=1
                self.valuar = True
                temp.parent.child[index+1] = Node(temp.parent)
                temp.parent.child[index+1].keys = temp.keys[int((self.degree)/2)+n:]
                keys = temp.keys
                child = temp.child
                if not ev:
                    temp.parent.child[index] = temp
                    temp.parent.child[index].keys = []
                else:
                    temp.parent.child[index] = Node(temp.parent)
                temp.parent.child[index].keys = keys[0:int((self.degree)/2)]
                
                if ev:
                    if len(child)>0:
                        if self.degree%2 == 0:
                            ii = int((len(child))/2)+1
                        else:
                            ii = int((len(child))/2)
                        temp.parent.child[index].leaf = False
                        temp.parent.child[index+1].leaf = False
                        for i in range(0, ii):
                            child[i].parent = temp.parent.child[index]
                            temp.parent.child[index].child.append(child[i])
                        for i in range(ii, len(child)):
                            child[i].parent = temp.parent.child[index+1]
                            temp.parent.child[index+1].child.append(child[i])
                else:
                    if len(temp.values):
                        temp.parent.child[index+1].values = {}
                        temp.parent.child[index].values = {}
                        for x in temp.parent.child[index+1].keys:
                            temp.parent.child[index+1].values[x] = v.get(x)
                        for x in temp.parent.child[index].keys:
                            temp.parent.child[index].values[x] = v.get(x)
                if  self.valuar and not ev:
                    temp.parent.child[index+1].next =temp.parent.child[index].next 
                    for i in range(0,len(temp.parent.child)-1):
                        temp.parent.child[i].next = temp.parent.child[i+1]
        return temp


    def delete(self, val):
        self.root = self._delete(self.root, str(val), None)
    
    def _delete(self, temp, key, copy):
        found = False
        if temp == self.root and not temp.child:
            if len(temp.keys)==1:
                temp = Node(None)
            else:
                temp.keys.remove(key)
                del temp.values[key]
            return temp
        if temp.child:
            for i in range(0, len(temp.keys)):
                if key in temp.keys:
                    copy = temp
                if key < temp.keys[i]:
                    found = True
                    self._delete(temp.child[i], key, copy)
                    temp = self.rotation(temp)
                    break
        if not found:
            if temp.child:
                self._delete(temp.child[len(temp.keys)], key, copy)
                temp = self.rotation(temp)
            else:
                if key not in temp.keys:
                    return False
                temp.keys.remove(key)
                del temp.values[key]
                if copy:
                    copy.keys.remove(key)
                    if len(temp.keys)!=0:
                        copy.insert(temp.keys[0], None)
                    elif temp.next:
                        if self.degree>4:
                            copy.insert(temp.next.keys[0], None)
                        else:
                            if copy!=temp.parent:
                                copy.insert(temp.next.keys[0], None)
                temp = self.rotation(temp)
        return temp
    
    #---------Rotaciones---------------#
    
    def rotation(self, temp):   
        if not len(temp.keys) and temp.parent:
            index = temp.parent.child.index(temp)
            if index== len(temp.parent.child)-1:
                if len(temp.keys)==0 and len(temp.parent.keys)==0:
                    if len(temp.parent.child[index-1].keys)>1:
                        temp = self.MoverIzquierda(temp,index)
                    else:
                        temp = self.UnirIzquierda(temp,index)
                else:
                    if len(temp.parent.child[index-1].keys) >1 and len(temp.parent.keys) >= 1 and len(temp.parent.child) == self.degree:
                        temp = self.MoverIzquierda(temp,index)
                    else:
                        if len(temp.parent.child[index-1].child) == self.degree:
                            temp = self.CambioRaizI(temp, index)
                        else:
                            temp = self.UnirIzquierdaRaiz(temp,index)
            elif not index:
                if len(temp.keys)==0 and len(temp.parent.keys)==0:
                    temp = self.UnirDerecha(temp,index)
                else:
                    if len(temp.parent.child[index+1].keys) >1 and len(temp.parent.keys) >= 1 and len(temp.parent.child) == len(temp.parent.keys)+1:
                        temp = self.MoverDerecha(temp,index)
                    else:
                        if len(temp.parent.child[index-1].child) == self.degree:
                            temp = self.CambioRaizI(temp, index)
                        else:
                            temp = self.UnirDerechaRaiz(temp, index)
                
            else:
                izquierda = len(temp.parent.child[index-1].keys)
                derecha = len(temp.parent.child[index+1].keys)
                if izquierda ==1 and len(temp.parent.keys)>0 and izquierda>=derecha:
                    temp = self.UnirIzquierda(temp,index)
                elif derecha ==1 and len(temp.parent.keys)>0 and derecha>izquierda:
                    temp = self.UnirDerecha(temp, index)
                elif izquierda>=derecha:
                    if len(temp.parent.child[index-1].child) == self.degree:
                        temp = self.CambioRaizI(temp, index)
                    else:
                        temp = self.MoverIzquierda(temp, index)
                elif derecha> izquierda:
                    if len(temp.parent.child[index+1].child) == self.degree:
                        print("Caso especial")
                    else:
                        temp = self.MoverDerecha(temp,index)
        elif temp.parent:
            index = temp.parent.child.index(temp)
            derecha = 0
            actual = len(temp.keys)
            izquierda = 0
            if index == len(temp.parent.child)-1:
                izquierda = len(temp.parent.child[index-1].keys)
                if izquierda+actual == self.degree-1 and actual+1 != izquierda and actual<izquierda:
                    temp = self.MoverIzquierda(temp,index)
                elif izquierda+actual < self.degree-1 and actual<izquierda:
                    temp = self.UnirIzquierda(temp,index)
            elif not index:
                derecha = len(temp.parent.child[index+1].keys)
                if derecha+actual == self.degree-1 and actual+1 != derecha and derecha>actual:
                    temp = self.MoverDerecha(temp,index)
                elif derecha+actual < self.degree-1 and actual<derecha:
                    temp = self.UnirDerecha(temp,index)
            else:
                izquierda = len(temp.parent.child[index-1].keys)
                derecha = len(temp.parent.child[index+1].keys)
                if izquierda+actual == self.degree-1 and actual+1 != izquierda and izquierda>actual:
                    temp = self.MoverIzquierda(temp,index)
                elif derecha+actual == self.degree-1 and actual+1 != derecha and actual<derecha:
                    temp = self.MoverDerecha(temp,index)
                elif izquierda+actual < self.degree-1 and actual< izquierda:
                    if len(temp.parent.child[index-1].child) == self.degree:
                        temp = self.CambioRaizI(temp, index)
                    else:
                        temp = self.UnirIzquierda(temp,index)
                elif derecha+actual < self.degree-1 and actual<derecha:
                    if len(temp.parent.child[index+1].child) == self.degree:
                        print("Caso especial")
                    else:
                        temp = self.UnirDerecha(temp,index)
        else:
            if len(temp.child)==1:
                if len(temp.keys)==1:
                    temp.child[0].insert(temp.keys[0])
                temp = temp.child[0]
                temp.parent = None
    
        return temp

    def CambioRaizI(self, temp, index):
        temp.parent.keys.remove(temp.parent.keys[index-1])
        temp.insert(temp.child[0].keys[0], None)
        val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
        temp.parent.insert(val, None)
        temp.parent.child[index-1].keys.remove(val)
        hijo = temp.parent.child[index-1].child[len(temp.parent.child[index-1].child)-1]
        temp.parent.child[index-1].child.remove(hijo)
        hijo.parent = temp
        temp.child.insert(0,hijo)
        return temp

    def UnirDerechaRaiz(self, temp, index):
        temp.keys = temp.parent.child[index+1].keys
        val = temp.parent.keys[0]
        if val not in temp.keys:
            temp.insert(val, temp.parent.values.get(val))
            if temp.parent.values.get(val):
                del temp.parent.values[val]
        temp.parent.keys.remove(val)
        for x in temp.parent.child[index+1].child:
            x.parent = temp
            temp.child.append(x)
        temp.next = temp.parent.child[index+1].next
        temp.values.update(temp.parent.child[index+1].values)
        temp.parent.child.remove(temp.parent.child[index+1])
        return temp

    def UnirIzquierdaRaiz(self, temp, index):
        val = temp.parent.keys[len(temp.parent.keys)-1]
        if val not in temp.parent.child[index-1].keys:
            temp.parent.child[index-1].insert(val, temp.parent.values.get(val))
            if temp.parent.values.get(val):
                del temp.parent.values[val]
            temp.parent.keys.remove(val)
        elif len(temp.parent.keys)>1:
            temp.parent.keys.remove(val)
        for x in temp.child:
            x.parent = temp.parent.child[index-1]
            temp.parent.child[index-1].child.append(x)
        temp.parent.child[index-1].next = temp.next
        temp.parent.child[index-1].values.update(temp.values)
        temp.parent.child.remove(temp)
        return temp

    def UnirIzquierda(self, temp, index):
        for x in temp.keys:
            temp.parent.child[index-1].insert(x, temp.values.get(x))
            if temp.values.get(x):
               del temp.values[x]
        for x in temp.child:
            x.parent = temp.parent.child[index-1]
            temp.parent.child[index-1].child.append(x)
        temp.parent.child[index-1].next = temp.next
        temp.parent.child.remove(temp)
        if len(temp.child)==1:
            if temp.child[0].keys[0] in temp.parent.keys:
                temp.parent.keys.remove(temp.child[0].keys[0])
                temp.parent.child[index-1].insert(temp.child[0].keys[0], None)
        else:
            temp = self.ReorganizarKeys(temp)
        return temp
    
    def UnirDerecha(self, temp, index):
        for x in temp.parent.child[index+1].keys:
            temp.insert(x, temp.parent.child[index+1].values.get(x))
            if temp.parent.child[index+1].values.get(x):
                del temp.parent.child[index+1].values[x]
        for x in temp.parent.child[index+1].child:
            x.parent = temp
            temp.child.append(x)
        temp.next = temp.parent.child[index+1].next
        temp.parent.child.remove(temp.parent.child[index+1])
        temp = self.ReorganizarKeys(temp)
        return temp
    
    def MoverDerecha(self, temp, index):
        val = temp.parent.child[index+1].keys[0]
        temp.insert(val, temp.parent.child[index+1].values.get(val))
        if temp.parent.child[index+1].values.get(val):
            del temp.parent.child[index+1].values[val]
        temp.parent.child[index+1].keys.remove(val)
        if temp.child and self.degree<5:
            hijo = temp.parent.child[index+1].child[0]
            temp.child.append(hijo)
            temp.parent.child[index+1].child.remove(hijo)
            hijo.parent = temp
        temp = self.ReorganizarKeys(temp)
        return temp

    def MoverIzquierda(self, temp, index):
        val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
        temp.insert(val, temp.parent.child[index-1].values.get(val))
        if temp.parent.child[index-1].values.get(val):
            del temp.parent.child[index-1].values[val]
        temp.parent.child[index-1].keys.remove(val)
        if temp.child and self.degree<5:
            hijo = temp.parent.child[index-1].child[len(temp.parent.child[index-1].child)-1]
            temp.child.insert(0,hijo)
            temp.parent.child[index-1].child.remove(hijo)
            hijo.parent = temp
        temp = self.ReorganizarKeys(temp)
        return temp

    def ReorganizarKeys(self, temp):
        temp.parent.keys = []
        for g in range(1,len(temp.parent.child)):
            temp.parent.insert(temp.parent.child[g].keys[0], None)
        return temp
    #---------Graficar-----------------#
    
    def graficar(self):
        f= open('archivo.dot', 'w',encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box];\n')
        f = self._graficar(f,self.root,'')
        lista = self._next('', self.root)
        lista1 = self._rank('{rank=same;', self.root)
        if lista!='':
            f.write(lista)
        if lista1!= '{rank=same;':
            f.write(lista1)
        f.write('}')
        f.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
        os.system('salida.png')
   
    def _graficar(self, f, temp, nombre):
        if temp:
            if nombre == '':
                nombre = "Nodo"+"D".join(str(x) for x in temp.keys)
            if len(temp.values):
                valor = ",".join(str(x) for x in temp.keys)+"\n"+",".join(str(x[1]) for x in temp.values.items())
            else:
                valor = ",".join(str(x) for x in temp.keys)
            f.write(nombre+' [ label = "'+valor+'"];\n')
            for c in temp.child:
                if c:
                    if len(c.child)==0:
                        nombre2 = "NodoH"+"D".join(str(x) for x in c.keys)
                    else:
                        nombre2 = "Nodo"+"D".join(str(x) for x in c.keys)
                    f = self._graficar(f, c, nombre2)
                    f.write(nombre+'->'+ nombre2+';\n')
        return f

    def _next(self, f, temp):
        if temp:
            if len(temp.child)==0 and temp!= self.root:
                nombre2 = "NodoH"+"D".join(str(x) for x in temp.keys)
                if temp.next:
                    f+=nombre2+'->'
                    f = self._next(f, temp.next)
                else:
                    f+=nombre2+';\n'
            else:
                if len(temp.child)!=0:
                    f = self._next(f, temp.child[0])
        return f
    
    def _rank(self, f, temp):
        if temp:
            if len(temp.child)==0 and temp!= self.root:
                nombre2 = "NodoH"+"D".join(str(x) for x in temp.keys)
                if temp.next:
                    f+=nombre2+';'
                    f = self._rank(f, temp.next)
                else:
                    f+=nombre2+'}\n'
            else:
                if len(temp.child)!=0:
                    f = self._rank(f,temp.child[0])
        return f

    def register(self, register):
        key = self.GenKey(register)
        self.insert(key, register)
    
    def GenKey(self, register):
        key = ''
        if len(self.PKey):
            if len(self.PKey)==1:
                key = register[self.PKey[0]]
            else:
                for x in self.PKey:
                    if self.PKey.index(x)==len(self.PKey)-1:
                        key+=str(register[x])
                    else:
                        key+= str(register[x])+'_'   
        else:
            key = self.Incremet
            self.Incremet+=1
        return key
    
    def buscar(self, register):
        key = self.GenKey(register)
        return self._buscar(self.root ,key)

    def _buscar(self, temp, key):
        if temp.child:
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    self._buscar(temp.child[i], key)
                    break
        else:
            if key in temp.keys:
                return temp
            else:
                return False