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


class ListaOrdenada:
    def __init__(self):
        self.cabeza=None
    def estaVacia(self):
        return self.cabeza==None

    def tamanio(self):
        actual=self.cabeza
        contador=0
        while actual!=None:
            contador=contador+1
            actual=actual.obtenerSiguiente()

        return contador

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

    def buscar(self,item):
        actual=self.cabeza
        encontrado=False
        detenerse=False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato()==item:
                encontrado=True
            else:
                if actual.obtenerDato() > item:
                    detenerse=True
                else:
                    actual=actual.obtenerSiguiente()
        return encontrado

    def agregar(self,item):
        actual=self.cabeza
        previo=None
        detenerse=False
        while actual != None and not detenerse:
            if actual.obtenerDato()>item:
                detenerse=True
            else:
                previo=actual
                actual=actual.obtenerSiguiente()

        temp=Nodo(item)

        if previo==None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza=temp

        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)


milista = ListaOrdenada()
milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)

print(milista.tamanio())
print(milista.buscar(93))
print(milista.buscar(100))
