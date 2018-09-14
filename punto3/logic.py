# from copy import deepcopy

def file_to_matrix(path):
    f = open ( path , 'r')
    m = [[int(num) for num in line.split(',')] for line in f ]
    return m

class Node:
    matrix = file_to_matrix('../enunciado/adyacencia_grafo_dirigido_con_pesos.csv')
    tags = 'ABCDEFGHIJKL'

    def __init__(self, tag=None, index=None):
        if tag:
            self.tag = tag
            self.index = self.tags.index(tag)
        elif index:
            self.tag = self.tags[index]
            self.index = index
        else: raise ValueError('tag not set')

    def __eq__(self, other):
        return self.tag == other.tag

    def __hash__(self):
        return hash(tuple(self.tag))

    def __repr__(self):
        return self.tag

    def children(self):
        children = []
        nodes_weights = self.matrix[self.index]
        for i in range(len(nodes_weights)):
            weight = nodes_weights[i]
            if weight != 0:
                new_node = Node(index=i)
                children.append(new_node)
        return children
