from code_challenges.graph_business.graph_trip import trip
from code_challenges.graphs.graph import Graph

def test_trip():
    graph = Graph()
    graph.add_node('Metroville')
    graph.add_node('Pandora')
    graph.add_edge('Metroville','Pandora',82)
    graph.add_node('Arendelle')
    graph.add_node('Monstropolis')
    graph.add_node('Naboo')
    graph.add_edge('Arendelle','Monstropolis',42)
    graph.add_edge('Monstropolis','Naboo',73)
    assert trip(graph,['Arendelle', 'Monstropolis','Naboo']) == 'True,$115'

def test_trip2():
    graph = Graph()
    graph.add_node('Metroville')
    graph.add_node('Pandora')
    graph.add_edge('Metroville','Pandora',82)
    graph.add_node('Arendelle')
    graph.add_node('Monstropolis')
    graph.add_node('Naboo')
    graph.add_edge('Arendelle','Monstropolis',42)
    graph.add_edge('Monstropolis','Naboo',73)
    assert trip(graph,['Metroville','Pandora']) == 'True,$82'

def test_trip3():
    graph = Graph()
    graph.add_node('Metroville')
    assert trip(graph,['Metroville']) == False