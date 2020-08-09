class Coladoble:
    def __init__(self):
        self.items=[]
    def agregarFrente(self,item):
        self.items.append(item)

    def agregarFinal(self,item):
        self.items.insert(0,item)

    def removerFrente(self):
        self.items.pop()

    def removerFinal(self):
        self.items.pop(0)

    def tamanio(self):
        return(len(self.items))
    def estaVacia(self):
        return self.items==[]

cd=Coladoble()

cd.agregarFinal(4)
cd.agregarFinal('perro')
cd.agregarFrente('gato')
cd.agregarFrente(True)
cd.agregarFinal(8.4)

cd.removerFinal()

print(cd.tamanio())
