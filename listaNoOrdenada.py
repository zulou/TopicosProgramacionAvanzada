class Nodo:
    def __init__(self,datoInicial):
        self.dato=datoInicial
        self.siguiente=None
    def obtenerDato(self):
        return self.dato
    def obtenerSiguiente(self):
        return self.siguiente
    def asignarDato(self,nuevoDato):
        self.dato=nuevoDato
    def asignarSiguiente(self,nuevoSiguiente):
        self.siguiente=nuevoSiguiente



class ListaNoOrdenada:
    def __init__(self):
        self.cabeza=None
    def estaVacia(self):
        return self.cabeza==None
    def agregar(self,item):
        temp=Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza=temp
    def tamanio(self):
        actual=self.cabeza
        contador=0
        while actual!=None:
            contador=contador+1
            actual=actual.obtenerSiguiente()

        return contador
    def buscar(self,item):
        actual=self.cabeza
        encontrado=False
        while item!=None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado=True
            else:
                actual=actual.obtenerSiguiente()
        return encontrado
    def remover(self,item):
        actual=self.cabeza
        previo=None
        encontrado=False
        while item!=None and not encontrado:
            if actual.obtenerDato()==item:
                encontrado=True
            else:
                previo=actual
                actual=actual.obtenerSiguiente()
        if previo==None:
            self.cabeza=actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente)




#NodoT=Nodo(30)
#print(NodoT.obtenerDato())
Lista=ListaNoOrdenada()
Lista.agregar(10)
Lista.agregar(20)
Lista.agregar(30)

Lista.agregar(40)

print(Lista.buscar(30))
print(Lista.tamanio())
