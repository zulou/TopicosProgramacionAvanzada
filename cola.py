class Cola:
    def __init__(self):
        self.items=[]
    def agregar(self,item):
        self.items.insert(0,item)
    def avanzar(self):
        self.items.pop()
    def estaVacia(self):
        self.items==[]
    def tamanio(self):
        return(len(self.items))

c = Cola()
c.agregar(3)
print(c.tamanio())
c.avanzar()
print(c.tamanio())
