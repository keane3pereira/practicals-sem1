import numpy as np

vertices = ["S", "A", "B", "C", "D", "G"]
edges = [
    ["S", "A", 1], ["S", "B", 5],
    ["A", "B", 2], ["A", "C", 2], ["A", "D", 1],
    ["B", "D", 2],
    ["C", "D", 3], ["C", "E", 1],
    ["D", "E", 2]
]

class Edge:
    def __init__(self, x, y, w):
        self.FROM = x
        self.TO = y
        self.WEIGHT = w
    
    def __repr__(self):
        return f"{self.FROM}-{self.TO}-{self.WEIGHT}"

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = [
            Edge(edge[0], edge[1], edge[2]) for edge in edges
        ]
        print(f"Edges: {self.edges}")
    
    def get_neighbours(self, vertex):
        neighbours = []
        for edge in self.edges:
            if edge.FROM == vertex: neighbours.append(edge)
        return neighbours
    

    def djikstra(self, start_vertex):
        current = start_vertex
        self.visited = []; self.queue = []
        self.costs = {current: 0}

        while len(self.visited) < len(self.vertices):
            ### add current to visited list
            self.visited.append(current)
            
            ### get adjacent vertices
            neighbours = self.get_neighbours(current)
            
            ### min(w(edge), w(current calculated))
            for neighbour in neighbours:
                calculate = self.costs[current] + neighbour.WEIGHT
                if neighbour.TO not in self.costs:
                    self.costs[neighbour.TO] = calculate
                else:
                    self.costs[neighbour.TO] = min(self.costs[neighbour.TO], calculate)

                ### if neighbour not in visited, insert to queue based on weight
                if neighbour.TO not in self.visited:
                    added = False
                    for i in range(len(self.queue)):
                        if neighbour.WEIGHT < self.queue[i].WEIGHT:
                            self.queue.insert(i, neighbour)
                            break
                    if not added:
                        self.queue.append(neighbour)
            
            print(f"{current} \t{self.costs}")
            
            ### set next current
            current = self.queue[0].TO
            ### remove first from queue
            self.queue.pop(0)

G = Graph(vertices, edges); start_vertex = "S"
G.djikstra(start_vertex)