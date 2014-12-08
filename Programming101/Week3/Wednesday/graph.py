class Graph:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self.edges:
            self.edges[node_a] = [node_b]
        elif node_a in self.edges:
            if node_b in self.edges[node_a]:
                return "Edge already exists."
            else:
                self.edges[node_a].append(node_b)
        if node_b not in self.edges:
            self.edges[node_b] = []
        return self.edges

    def get_neighbours_for(self, node):
        if node not in self.edges:
            return "Node not in neighbours list."
        return self.edges[node]

    def path_between(self, node_a, node_b):
        if node_a not in self.edges or node_b not in self.edges:
            return False
        neighbours = self.get_neighbours_for(node_a)
        if node_b in neighbours:
            return True

        for neighbour in neighbours:
            if self.path_between(neighbour, node_b):
                return True
        return False
