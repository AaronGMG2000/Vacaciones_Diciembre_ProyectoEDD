import pickle
import os

def Read(direction, name):
    with open(direction+name+".bin","rb") as f:
        fil = pickle.load(f)
        f.close()
    return fil
def delete(direction):
    for f in os.listdir(direction):
        if not f.endswith(".bin"):
            _dropAll(direction+"/"+f)
            os.rmdir(direction+"/"+f)
        else:
            os.remove(os.path.join(direction, f))
    os.rmdir(direction)
    
def _dropAll(nombre):
    for f in os.listdir(nombre):
        if not f.endswith(".bin"):
            _dropAll(nombre+"/"+f)
            os.rmdir(nombre+"/"+f)
        else:
            os.remove(os.path.join(nombre, f))

def write(direction, name, data):
    dire = direction+name
    os.mkdir(dire)
    with open(dire+"/"+name+".bin","wb") as ff:
        pickle.dump(data, ff)
        ff.close()

def update(direction, name, data):
    with open(direction+name+".bin","wb") as ff:
        pickle.dump(data, ff)
        ff.close()
