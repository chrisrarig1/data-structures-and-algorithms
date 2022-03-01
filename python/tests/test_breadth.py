from code_challenges.__init__ import __version__
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_single_breadth():
    bt = BinaryTree()
    node = Node('Todd')
    bt.root = node
    assert breadth_first(bt) == ["Todd"]

def test_breadth():
    coors = Node('coors')
    busch = Node('busch')
    yueng = Node('yueng')
    bt = BinaryTree(coors)
    bt.root.left = busch
    bt.root.right = yueng
    assert breadth_first(bt) == ['coors']
