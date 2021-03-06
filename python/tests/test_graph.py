from code_challenges.graphs.graph import Graph
import pytest

# Node can be successfully added to the graph
def test_node():
    graph = Graph()
    assert graph.add_node('a').value == 'a'
    assert graph.adja_list == {'a': []}
# An edge can be successfully added to the graph
def test_edges():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('b','a',4)
    assert graph.adja_list['a']==[['b',4]]
    assert graph.adja_list['b']==[['a',4]]
# A collection of all nodes can be properly retrieved from the graph
def test_nodes():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    assert graph.get_node() == ['a','b','c']
# All appropriate neighbors can be retrieved from the graph
def test_neighbors():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge('b','a',4)
    graph.add_edge('c','a',5)
    assert graph.get_neighbor('a') == [['b', 4], ['c', 5]]
# The proper size is returned, representing the number of nodes in the graph
def test_size():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    assert graph.size() == 3
# A graph with only one node and edge can be properly returned
def test_one_edge():
    graph = Graph()
    graph.add_node('a')
    graph.add_edge('a','a',4)
    assert graph.adja_list['a']==[['a',4]]
# An empty graph properly returns null
def test_empty():
    graph = Graph()
    assert graph.size() == None

def test_breadth_empty():
    graph = Graph()
    assert graph.breadth_first('a') == None

def test_breadth_single():
    graph = Graph()
    graph.add_node('a')
    assert graph.breadth_first('a') == ['a']

def test_breadth():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge('b','a',4)
    graph.add_edge('c','a',5)
    assert graph.breadth_first('a') == ['a','b','c']

def test_depth_one():
    graph = Graph()
    graph.add_node('a')
    assert graph.depth_first('a') == 'a'

def test_depth_not_connected():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('c')
    graph.add_node('b')
    graph.add_edge('b','a',4)
    assert graph.depth_first('c') == 'c'


def test_depth_full():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_edge('b','a',4)
    graph.add_edge('c','a',5)
    graph.add_edge('c','d',5)
    assert graph.depth_first('a') == ['a', 'b', 'c', 'd']

