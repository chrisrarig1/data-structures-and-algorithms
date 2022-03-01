from code_challenges.__init__ import __version__
from code_challenges.tree_fizz_buzz.fizz_buzz import Node,fizz_buzz,fizz_buzz_tree

def test_version():
    assert __version__ == '0.1.0'

def test_fizz_buzz():
    tree = Node(3)
    child_1 = Node(5)
    child_2 = Node(15)
    child_3 = Node(8)
    tree.add_child(child_1)
    tree.add_child(child_2)
    tree.add_child(child_3)
    new_tree = fizz_buzz_tree(tree)
    assert tree.children[0].value == 5
