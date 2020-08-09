from binarytree import  tree
class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1


class BinomialHeap:
    def __init__(self):
        self.trees = []

    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)

        return smallest_node.key

    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least

    def combine_roots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)


    def show_nodes(self):
        #self.merge()
        tr=self.trees
        #self.merge(tr)
        i=0
        for arbol in tr:
            print('la Raiz del arbol {} e: {}'.format(arbol.key,arbol.order))
            for index, t in enumerate(arbol.children):
                print('{:8d}{:12d}{:8d}'.format(index, t.key, t.order))



            #for childs in arbol.children:
            #    print(childs)
            #print(arbol.children)
            #i+=1

            #print(arbol.key)


    def merge(self, h):
        self.combine_roots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1
                    and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i = i + 1

        #self.mostrar_nodos(h)



    def insert(self, key):
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)




bheap = BinomialHeap()
bheap.insert(77)
bheap.insert(21)
bheap.insert(46)
bheap.insert(90)
bheap.insert(9)
bheap.insert(92)
bheap.insert(64)
bheap.insert(81)
bheap.insert(44)
bheap.insert(89)
bheap.insert(47)
bheap.insert(11)
bheap.insert(43)


#for test in bheap.trees:
#    for x,y in  enumerate(test.children):
#        print(y.key)
#        for z,t in enumerate(y.children):
#            print(t.key)
#        #print(x)
while True:
    do = input('Opciones: ').split()

    operation = do[0].strip().lower()
    if operation == 'insertar':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'min':
        print('el valor minimo es: {}'.format(bheap.get_min()))
    elif operation == 'extract':
        print('El valor minimo fue removido {}'.format(bheap.extract_min()))
    elif operation == 'mostrar':
        bheap.show_nodes()

    elif operation == 'salir':
        break
