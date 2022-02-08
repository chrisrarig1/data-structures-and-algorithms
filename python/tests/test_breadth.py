from code_challenges.__init__ import __version__
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_breadth():
    node1 = Node(21)
    bt = BinaryTree(node1)
    node2 = Node(32)
    node3 = Node(17)
    node4 = Node(30)
    node5 = Node(18)
    node1.left = node2
    node1.left.left = node4
    node1.right = node3
    node1.right.right = node5
    assert breadth_first(node1) == [21]
