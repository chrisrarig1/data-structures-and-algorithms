class Graph:

    def __init__(self):
        self.adja_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        if vertex.value in self.adja_list:
            return "This vertex already exists"
        else: 
            self.adja_list[vertex.value] = []
            return self.adja_list[vertex.value]

    def add_edge(self,v1,v2,edge):

        if v1 and v2 in self.adja_list:
            edge1 = Edge(v2,edge)
            edge2 = Edge(v1,edge)
            if v1 == v2:
                self.adja_list[v1].append(edge1.vertex)
                self.adja_list[v1].append(edge1.weight)
            else:
                self.adja_list[v1].append(edge1.vertex)
                self.adja_list[v1].append(edge1.weight)
                self.adja_list[v2].append(edge2.vertex)
                self.adja_list[v2].append(edge2.weight)
        else:
            return 'Please add vertices'

    def get_node(self):
        nodes = []
        for i in self.adja_list:
            nodes.append(i)
        return nodes
        # return self.adja_list.keys()

    def get_neighbor(self, v):
        # neighbors = []
        # for i in self.adja_list[v]:
        #     neighbors.append(i)
        # if len(neighbors)> 0:
        #     return neighbors
        # else:
        #     return 'No neighbors'
        if len(self.adja_list[v]) == 0:
            return 'No neighbors'
        else:
            return self.adja_list[v]


    def size(self):
        if len(self.adja_list) == 0:
            return None
        else:
            return len(self.adja_list)



class Vertex:
    def __init__(self, value):
        self.value = value
        

class Edge:
    def __init__(self, vertex, weight=1):
        self.weight = weight
        self.vertex = vertex




graph = Graph()
graph2 = Graph()

graph.add_node('b')
graph.add_node('c')

print(graph.add_node('a'))
graph.add_edge('b','a',4)
print(graph.adja_list['a'])
print(graph.get_node())
print(graph.get_neighbor('a'))
print(graph.get_neighbor('c'))
print(graph.size())
print(graph2.size())