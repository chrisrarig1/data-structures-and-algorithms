from code_challenges.graphs.graph import Graph


def trip(graph, cities):
    direct = graph.get_neighbor(cities[0])
    if direct == 'No neighbors':
        return False
    poss = False
    cost = 0
    for i in range(1,len(cities)):
        for x in direct:
            if cities[i] == x[0]:
                poss = True
                cost += x[1]
        direct = graph.get_neighbor(cities[i])
    return f'{poss},${cost}'


