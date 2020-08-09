class Pila:
    def __init__(self):
        self.items=[]
    def estaVacia(self):
        return self.items==[]
    def incluir(self,item):
        self.items.append(item)
    def extraer(self):
        print(self.items[len(self.items)-1])
        #print(self.items.pop())
        self.items.pop()
    def inspeccionar(self):
        return self.items[len(self.items)-1]
    def tamanio(self):
        return len(self.items)


a=Pila()

a.incluir('a')
a.incluir('b')
a.incluir('c')
a.incluir('d')
a.incluir('e')
while not a.estaVacia():
    a.extraer()

print(a.tamanio())
