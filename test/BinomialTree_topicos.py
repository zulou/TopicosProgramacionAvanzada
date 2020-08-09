class BinomialTree:
    def __init__(self,valor):
        self.valor=valor
        self.hijo=[]
        self.orden=0
    def agregar_al_final(self,t):
        self.hijo.append(t)
        self.orden=self.orden+1

trees=[]
while True:


    entrada = input('opciones: ').split()
    #print(entrada)
    #entrada=input('Ingrese').split()
    #print(entrada[0])
    opciones=entrada[0].strip().lower()

    if opciones == 'crear':
        key = int(entrada[1])
        btree = BinomialTree(key)
        trees.append(btree)
       #print('Binomial tree created.')
        #print(trees[0])
    elif opciones == 'combinar':
        index1 = int(entrada[1])
        index2 = int(entrada[2])

        if trees[index1].orden == trees[index2].orden:
            trees[index1].agregar_al_final(trees[index2])
            del trees[index2]
            print('Arbol Binomial Combinado')
        else:
            print('El orden de los arboles Binomiales tiene que ser el mismo')
    elif opciones == 'salir':
        break
    print('{:>8}{:>12}{:>8}'.format('Indice', 'Nodo Raiz', 'Orden'))
    for index, t in enumerate(trees):
        print('{:8d}{:12d}{:8d}'.format(index, t.valor, t.orden))

