# from copy import deepcopy

def file_to_matrix(path):
    f = open ( path , 'r')
    m = [[int(num) for num in line.split(',')] for line in f ]
    return m

matrix = file_to_matrix('../enunciado/adyacencia_grafo_dirigido_con_pesos.csv')

class AStar:
    def __init__(self, start, distance_finder, heuristic):
        self.start = start
        self.distance_finder = distance_finder
        self.heuristic = heuristic
        
    def __get_new_current(self, open_set, f_score):
        lowest = float('inf')
        new_current = None
        for node in open_set:
            if f_score[node] < lowest:
                lowest = f_score[node]
                new_current = node
        return new_current

    def __reconstruct_path(self, parents, current):
        total_path = [current]
        for k in parents.keys():
            current = parents[current]
            total_path.append(current)
            if current == self.start: break
        return total_path

    def evaluate(self, goal):
        self.heuristic.desired_state = goal
        # closed_set: the set of nodes already evaluated
        closed_set = []
        # open_set: the set of currently discovered nodes that are not evaluated yet
        open_set = [self.start]
        parents = {}
        g_score = {}
        g_score[self.start] = 0
        f_score = {}
        f_score[self.start] = self.heuristic.estimate(self.distance_finder, self.start)
        while open_set:
            current = self.__get_new_current(open_set, f_score)
            if current == goal:
                return self.__reconstruct_path(parents, current)
            open_set.remove(current)
            closed_set.append(current)
            children = current.children()
            for child in children:
                if not child in closed_set:
                    temp_score = g_score[current] + self.distance_finder.distance(current, child)
                    new_node = not child in open_set
                    if new_node: open_set.append(child)
                    if new_node or temp_score < g_score[child]:
                        parents[child] = current
                        g_score[child] = temp_score
                        f_score[child] = g_score[child] + self.heuristic.estimate(self.distance_finder, child)

class Node:
    def __init__(self, tag=None, index=None):
        if tag:
            self.tag = tag
            self.index = self.tags.index(tag)
        elif index:
            self.tag = self.tags[index]
            self.index = index
        else: raise ValueError('tag not set')
        self.matrix = None
        self.tags = None

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
    