class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1


trees = []



while True:
    do = input('').split()

    operation = do[0].strip().lower()
    print(do[0].strip().lower())
    #print(operation)

    if operation == 'crear':
        key = int(do[1])
        btree = BinomialTree(key)
        trees.append(btree)
       #print('Binomial tree created.')
        print(trees[0])
    elif operation == 'combinar':
        index1 = int(do[1])
        index2 = int(do[2])

        if trees[index1].order == trees[index2].order:
            trees[index1].add_at_end(trees[index2])
            del trees[index2]
            print('Binomial trees combined.')
        else:
            print('Orders of the trees need to be the same.')

    elif operation == 'quit':
        break

    print('{:>8}{:>12}{:>8}'.format('Indice', 'Valor', 'Orden'))
    for index, t in enumerate(trees):
        print('{:8d}{:12d}{:8d}'.format(index, t.key, t.order))
