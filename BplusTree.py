import os
import random

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.keys = []
        self.child = []
        self.next = None
        self.leaf = True
    
    def insert(self, key):
        self.keys.append(key)
        if len(self.keys) > 1:
            self.keys.sort()
    
    def compare(self, value):
        length = len(self.keys)
        if self.child == [] or value in self.keys:
            return None
        
        for i in range(length):
            if value < self.keys[i]:
                return i
        return i + 1    
 
    def getPos(self):
        if self.parent:
            return self.parent.child.index(self)

class BPlusTree:

    def __init__(self, degree):
        self.root = Node(None)
        self.degree = degree
        self.valuar = False
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.valuar = False
    
    def _insert(self, temp, key):
        if temp.leaf:
            temp.insert(key)
        else:
            found = False
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    found = True
                    self._insert(temp.child[i], key)
                    break
            if not found:
                self._insert(temp.child[len(temp.keys)], key)

        if len(temp.keys) == self.degree:
            if temp.parent == None:
                c = temp
                temp = Node(None)
                temp.insert(c.keys[int((self.degree)/2)])
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
                temp.leaf = False
            else:
                n = 0
                ev = False
                if self.valuar:
                        n = 1
                        ev = True
                        self.valuar = False
                mkey = temp.keys[int((self.degree)/2)]
                temp.parent.insert(mkey)
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
                if  self.valuar and not ev:
                    temp.parent.child[index+1].next =temp.parent.child[index].next 
                    for i in range(0,len(temp.parent.child)-1):
                        temp.parent.child[i].next = temp.parent.child[i+1]
        return temp


    def delete(self, val):
        self.root = self._delete(self.root, val, None)
    def _delete(self, temp, key, copy):
        found = False
        if temp == self.root and not temp.child:
            temp = Node(None)
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
                if copy:
                    copy.keys.remove(key)
                index = temp.parent.child.index(temp)
                if key in temp.keys and len(temp.keys) == 1:
                    if len(temp.parent.child) == self.degree:
                        temp.keys.remove(key)
                        if len(temp.parent.keys) != self.degree-1:
                            if index == int((self.degree-1)/2):
                                if len(temp.parent.child[index-1].keys)> len(temp.parent.child[index+1].keys):
                                    temp.parent.insert(temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1])
                                    j = len(temp.parent.child[index-1].keys)-1
                                    temp.insert(temp.parent.child[index-1].keys[j])
                                    temp.parent.child[index-1].keys.remove(temp.parent.child[index-1].keys[j])
                                    if not len(temp.parent.child[index-1].keys):
                                        temp.parent.child[index-1].next = temp.next
                                        temp.parent.child[index-1].keys = temp.keys
                                        if copy!=temp.parent:
                                            temp.parent.keys.remove(temp.keys[0])
                                        temp.parent.child.remove(temp.parent.child[index])
                                elif len(temp.parent.child[index-1].keys)< len(temp.parent.child[index+1].keys):
                                    temp.parent.insert(temp.parent.child[index+1].keys[1])
                                    temp.insert(temp.parent.child[index+1].keys[0])
                                    temp.parent.child[index+1].keys.remove(temp.parent.child[index+1].keys[0])
                                    if not len(temp.parent.child[index+1].keys):
                                        temp.parent.child[index+1].next = temp.next
                                        temp.parent.child[index+1].keys = temp.keys
                                        if copy!=temp.parent:
                                            temp.parent.keys.remove(temp.keys[0])
                                else:
                                    if copy!=temp.parent:
                                        temp.parent.keys.remove(temp.keys[0])
                                    if temp.next:
                                        temp.parent.child[index-1].next = temp.next
                                    temp.parent.child.remove(temp)
                            elif index == self.degree-1:
                                if len(temp.parent.child[index-1].keys)==1:
                                    if copy != temp.parent:
                                        temp.parent.keys.remove(key)
                                    temp.parent.child.remove(temp)
                                    temp.parent.child[index-1].next = temp.next
                                else:
                                    val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
                                    temp.insert(val)
                                    temp.parent.child[index-1].keys.remove(val)
                                    if copy!=temp.parent:
                                        copy.keys.remove(key)
                                    temp.parent.insert(val)
                            else:
                                if temp.next:
                                    temp.parent.insert(temp.next.keys[len(temp.next.keys)-1])
                        else:
                            if temp.next and copy:
                                copy.insert(temp.next.keys[0])
                            if index+1 != len(temp.parent.child):
                                temp.insert(temp.parent.child[index+1].keys[0])
                                temp.next.keys.remove(temp.keys[0])
                                k = temp.parent.child.index(temp)
                                temp.parent.keys.remove(temp.keys[0])
                                if len(temp.next.keys):
                                    temp.parent.keys.insert(k,temp.next.keys[0])
                            else:
                                temp.parent.child.remove(temp)
                                temp.parent.child[index-1].next = None
                        if temp.next:
                            if not len(temp.next.keys):
                                # temp.parent.keys.remove(temp.keys[len(temp.keys)-1])
                                temp.parent.child.remove(temp.next)
                                temp.next = temp.parent.child[index+1]
                    else: 
                        if index:
                            temp.parent.child[index-1].next = temp.parent.child[index].next
                        if index+1 != len(temp.parent.child):
                            if temp.next and copy:
                                copy.insert(temp.next.keys[0]) 
                            temp.keys.remove(key)
                            temp.insert(temp.parent.child[index+1].keys[0])
                            temp.parent.child[index+1].keys.remove(temp.keys[len(temp.keys)-1])
                            temp.parent.keys.remove(temp.keys[0])
                            if len(temp.parent.child[index+1].keys):
                                temp.parent.insert(temp.parent.child[index+1].keys[0])
                            else:
                                if temp.next:
                                    temp.next = temp.next.next
                            if not len(temp.parent.child[index+1].keys):
                                temp.parent.child.remove(temp.parent.child[index+1])
                        else:
                            temp.parent.child.remove(temp)
                else:
                    num = temp.keys.index(key)
                    t = len(temp.keys)
                    temp.keys.remove(key)
                    if num+1 != t:
                        if len(temp.child) == self.degree:
                            temp.parent.insert(temp.next.keys[num])
                        else:
                            if copy:
                                copy.insert(temp.keys[num])
                            if index!= len(temp.parent.child)-1:
                                izquierda = len(temp.parent.child[index-1].keys)
                                derecha = len(temp.parent.child[index+1].keys)
                                actual = len(temp.keys)
                                if izquierda<=derecha and izquierda+actual< self.degree and izquierda!=actual:
                                    for x in temp.keys:
                                        temp.parent.child[index-1].insert(x)
                                    temp.parent.child[index-1].next = temp.next
                                    temp.parent.keys.remove(temp.keys[0])
                                    temp.parent.child.remove(temp)
                                elif actual+derecha< self.degree and derecha> izquierda and derecha!=actual:
                                    for x in temp.keys:
                                        temp.parent.child[index+1].isnsert(x)
                                    temp.parent.child[index+1].next = temp.next
                                    temp.parent.keys.remove(temp.keys[0])
                                    temp.parent.child.remove(temp)
                    else:
                        if index!= len(temp.parent.child)-1:
                            izquierda=0
                            if index:
                                izquierda = len(temp.parent.child[index-1].keys)
                            derecha = len(temp.parent.child[index+1].keys)
                            actual = len(temp.keys)
                            if len(temp.parent.child) == self.degree:
                                if len(temp.parent.keys)!= self.degree-1:
                                    temp.parent.insert(temp.next.keys[0])
                                if (actual+izquierda)== self.degree-1:
                                    val = temp.parent.child[index-1].keys[izquierda-1]
                                    temp.parent.keys.remove(temp.keys[0])
                                    temp.parent.insert(val)
                                    temp.insert(val)
                                    temp.parent.child[index-1].keys.remove(val)
                                elif (actual+derecha) == self.degree-1:
                                    val = temp.parent.child[index+1].keys[0]
                                    temp.parent.keys.remove(val)
                                    temp.parent.child[index+1].keys.remove(val)
                                    temp.parent.insert(temp.parent.child[index+1].keys[0])
                                    temp.insert(val)
                            else:
                                if len(temp.parent.keys)+1!= len(temp.parent.child):
                                    temp.parent.insert(temp.next.keys[0])
                                if izquierda!=derecha and (actual+izquierda) == self.degree-1 and actual!=izquierda:
                                    val = temp.parent.child[index-1].keys[izquierda-1]
                                    temp.parent.keys.remove(temp.keys[0])
                                    temp.parent.insert(val)
                                    temp.insert(val)
                                    temp.parent.child[index-1].keys.remove(val)
                                elif izquierda!=derecha and (actual+derecha) == self.degree-1 and actual!=derecha:
                                    val = temp.parent.child[index+1].keys[0]
                                    temp.parent.keys.remove(val)
                                    temp.parent.child[index+1].keys.remove(val)
                                    temp.parent.insert(temp.parent.child[index+1].keys[0])
                                    temp.insert(val)
                        else:
                            izquierda = len(temp.parent.child[index-1].keys)
                            actual = len(temp.keys) 
                            if len(temp.parent.keys)+1!= len(temp.parent.child):
                                    temp.parent.insert(temp.next.keys[0])
                            if (actual+izquierda) == self.degree-1 and actual!=izquierda:
                                val = temp.parent.child[index-1].keys[izquierda-1]
                                temp.parent.keys.remove(temp.keys[0])
                                temp.parent.insert(val)
                                temp.insert(val)
                                temp.parent.child[index-1].keys.remove(val)
                            elif actual!=izquierda:
                                for x in temp.keys:
                                        temp.parent.child[index-1].insert(x)
                                temp.parent.child[index-1].next = temp.next
                                temp.parent.keys.remove(temp.keys[0])
                                temp.parent.child.remove(temp)
                            

                    
        return temp
    #---------Rotaciones---------------#
    def rotation(self, temp):   
        if not len(temp.keys):
            if temp.parent:
                if len(temp.parent.keys) == 1:
                    der = len(temp.parent.child[1].keys)
                    iz = len(temp.parent.child[0].keys)
                    index = temp.parent.child.index(temp)
                    if index+1 != len(temp.parent.child):
                        temp.insert(temp.parent.keys.pop())
                        if der==1 and iz==0:
                            temp.insert(temp.parent.child[index+1].keys.pop())
                            for c in temp.parent.child[index+1].child:
                                c.parent = temp
                                temp.child.append(c)
                            temp.parent.child = []
                            temp.parent.child.append(temp)
                        else:
                            val = temp.parent.child[index+1].keys[0]
                            temp.parent.insert(val)
                            temp.parent.child[index+1].keys.remove(val)
                            hijo = temp.parent.child[index+1].child[0]
                            temp.child.append(hijo)
                            temp.parent.child[index+1].child.remove(hijo)
                            hijo.parent = temp
                    else:
                        if temp.parent == self.root:
                            temp.insert(temp.parent.keys[0])
                            temp.parent.keys = []
                        else:
                            index = temp.parent.child.index(temp)
                            if index:
                                temp.parent.keys.remove(temp.child[0].keys[0])
                                temp.insert(temp.child[0].keys[0])
                                val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
                                temp.parent.insert(val)
                                temp.parent.child[index-1].keys.remove(val)
                                hijo = temp.parent.child[index-1].child[len(temp.parent.child[index-1].child)-1]
                                temp.parent.child[index-1].child.remove(hijo)
                                hijo.parent = temp
                                temp.child.insert(0,hijo)
                            else:
                                temp.insert(temp.child[0].keys[len(temp.child[0].keys)-1])
                                hijo = Node(temp)
                                hijo.insert(temp.keys[0])
                                temp.child[0].keys.remove(temp.keys[0])
                                temp.child.append(hijo)
                                temp.child[0].next = hijo
                else:
                    index = temp.parent.child.index(temp)
                    if index+1 == len(temp.parent.child):
                        temp.parent.child[index-1].insert(temp.child[0].keys[0])
                        temp.parent.child[index-1].child.append(temp.child[0])
                        temp.child[0].parent = temp.parent.child[index-1]
                        temp.parent.keys.remove(temp.child[0].keys[0])
                        temp.parent.child.remove(temp)
                        temp = None
                    else:
                        if index:
                            if len(temp.child[0].keys)!=1 and len(temp.child) == 1:
                                val = temp.child[0].keys[len(temp.child[0].keys)-1]
                                temp.insert(val)
                                temp.child[0].keys.remove(val)
                                temp.child.append(Node(temp))
                                if temp.child[0].next:
                                    temp.child[1].insert(val)
                                    temp.child[1].next = temp.child[0].next
                                    temp.child[0].next = temp.child[1]
                            elif len(temp.parent.child[index-1].keys):
                                index = temp.parent.child.index(temp)
                                izquierda = 0
                                derecha = 0
                                con = False
                                if index+1 == len(temp.parent.child):
                                    izquierda = len(temp.parent.child[index-1].keys)
                                else:
                                    izquierda = len(temp.parent.child[index-1].keys)
                                    derecha = len(temp.parent.child[index+1].keys)
                                if izquierda==derecha==1:
                                    con = True
                                if len(temp.child) ==1 and not con:
                                        if izquierda>derecha or izquierda!=1:
                                            temp.parent.keys.remove(temp.child[0].keys[0])
                                            val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
                                            temp.parent.insert(val)
                                            temp.parent.child[index-1].keys.remove(val)
                                            temp.insert(temp.child[0].keys[0])
                                            hijo = temp.parent.child[index-1].child[len(temp.parent.child[index-1].child)-1]
                                            temp.child.insert(0,hijo)
                                            hijo.parent = temp
                                            temp.parent.child[index-1].child.remove(hijo)
                                        else:
                                            temp.parent.keys.remove(temp.child[0].next.keys[0])
                                            val = temp.parent.child[index+1].keys[0]
                                            temp.parent.insert(val)
                                            temp.parent.child[index+1].keys.remove(val)
                                            temp.insert(temp.child[0].next.keys[0])
                                            hijo = temp.parent.child[index+1].child[0]
                                            temp.child.append(hijo)
                                            hijo.parent = temp
                                            temp.parent.child[index+1].child.remove(hijo)
                                else:
                                    temp.parent.child[index-1].insert(temp.child[0].keys[0])
                                    temp.parent.child[index-1].child.append(temp.child[0])
                                    temp.child[0].parent = temp.parent.child[index-1]
                                    temp.parent.keys.remove(temp.child[0].keys[0])
                                    temp.parent.child.remove(temp)
                                    temp = None
                        
                        else:
                            temp.parent.child[index+1].insert(temp.parent.keys[0])
                            temp.parent.child[index+1].child.insert(0, temp.child[0])
                            temp.child[0].parent = temp.parent.child[index+1]
                            temp.parent.keys.remove(temp.parent.keys[0])
                            temp.parent.child.remove(temp)
                            temp = None
            else:
                if len(temp.child) == 1:
                    if len(temp.child[0].keys)==1:
                        temp = temp.child[0]
                        temp.parent = None
                        temp.next = None
                    else:
                        val = temp.child[0].keys[len(temp.child[0].keys)-1]
                        temp.insert(val)
                        temp.child[0].keys.remove(val)
                        hijo = Node(temp)
                        temp.child[0].next = hijo
                        hijo.insert(val)
                        temp.child.append(hijo)
                else:
                    hijoI = temp.child[0]
                    hijoD = temp.child[1]
                    if len(hijoI.keys) == len(hijoD.keys):
                        hijoI.insert(hijoD.keys[0])
                        for c in hijoD.child:
                            c.parent = hijoI
                            hijoI.child.append(c)
                        hijoD = None
                        temp = hijoI
                        temp.parent = None
                    else:
                        if len(hijoI.keys) > len(hijoD.keys):
                            val = hijoI.keys[len(hijoI.keys)-1]
                            temp.insert(val)
                            hijoI.keys.remove(val)
                            hijoD.child.insert(0,hijoI.child[len(hijoI.child)-1])
                            hijoD.child[0].parent = hijoD
                            hijoI.child.remove(hijoD.child[0])
                        else:
                            val = hijoI.keys[len(hijoD.keys)-1]
                            temp.insert(val)
                            hijoD.keys.remove(val)
                            hijoI.append(hijoI.child[0])
                            hijoI.child[len(hijoI.child)-1].parent = hijoI
                            hijoD.child.remove(hijoD.child[0])
        else:
            if temp.parent:
                if len(temp.parent.child) == self.degree:
                    if len(temp.parent.keys) != self.degree-1:
                        index = temp.parent.child.index(temp)
                        if len(temp.keys) == 1:
                            if index == self.degree-1:
                                temp.parent.child[index-1].insert(temp.keys[0])
                                temp.parent.child[index-1].child.append(temp.child[0])
                                temp.child[0].parent = temp.parent.child[index-1]
                                temp.parent.child.remove(temp)
                                temp = None
            
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
            f.write(nombre+' [ label = "'+",".join(str(x) for x in temp.keys)+'"];\n')
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

    

t = BPlusTree(3)
# lista = []
lista = [98, 295, 77, 105, 238, 75, 171, 101,129, 109, 199, 178, 53, 279, 192, 257, 34, 63, 158, 0, 121, 31]
for l in lista:
    t.insert(l)
t.delete(129)
t.delete(98)
t.delete(101)
t.delete(75)
t.delete(192)
t.delete(238)
t.delete(158)
# t.delete(105)
# t.delete(171)
# t.delete(109)
# t.delete(178)
# t.delete(75)
# t.delete(192)
# t.delete(77)
# t.delete(121)
# t.delete(238)
# t.delete(257)
# t.delete(279)
# t.delete(199)
# t.delete(53)
# t.delete(295)
# t.delete(63)
# t.delete(34)
# t.delete(0)
# t.delete(31)
# for i in range(1,25):
#     d = random.randrange(300)
#     if d not in lista:
#         t.insert(d)
#         lista.append(d)
#     else:
#         i-=1
print(lista)
# t.delete(171)
# t.delete(178)
# t.delete(192)
# t.delete(105)
# t.delete(109)
# t.delete(121)
# t.delete(129)
# t.delete(158)
# t.delete(75)
# t.delete(199)
# t.delete(77)
# t.delete(238)
# t.delete(98)
# t.delete(257)
# t.delete(53)
# t.delete(279)
# t.delete(63)
# t.delete(101)
# t.delete(31)
# t.delete(295)
# t.delete(34)
# t.delete(0)

# for i in range(5,11):
#     t.insert(i)
t.graficar()