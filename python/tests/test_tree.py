from code_challenges.__init__ import __version__
from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.binary_search_tree import BinarySearchTree
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_node():
    node = Node(12)
    actual = node.value
    expected = 12
    assert actual == expected

# Can successfully instantiate an empty tree
def test_empty():
    bt = BinaryTree()
    assert bt
# Can successfully instantiate a tree with a single root node
def test_root():
    bt = BinaryTree()
    assert bt.root == None

def test_child_preorder():
    coors = Node('coors')
    busch = Node('busch')
    yueng = Node('yueng')

    bt = BinaryTree(coors)
    coors.left = busch
    coors.right = yueng
    assert coors.left == bt.root.left
    assert coors.right == yueng
    order_list = bt.pre_order()
    assert order_list == ['coors','busch','yueng']

def test_child_inorder():
    coors = Node('coors')
    busch = Node('busch')
    yueng = Node('yueng')

    bt = BinaryTree(coors)
    coors.left = busch
    coors.right = yueng
    assert coors.left == bt.root.left
    assert coors.right == yueng
    order_list = bt.in_order()
    assert order_list == ['busch','coors','yueng']

def test_child_post_order():
    coors = Node('coors')
    busch = Node('busch')
    yueng = Node('yueng')

    bt = BinaryTree(coors)
    coors.left = busch
    coors.right = yueng
    assert coors.left == bt.root.left
    assert coors.right == yueng
    order_list = bt.post_order()
    assert order_list == ['busch','yueng','coors']

def test_bst_root_none():
    bt = BinarySearchTree()
    assert bt.root == None

def test_bst_root_add():
    node1 = Node(21)
    node2 = Node(11)
    node1.left = node2
    bts = BinarySearchTree(node1)
    bts.add(22)
    assert bts.post_order() == [22,11,21]

def test_contains_false():
    node1 = Node(21)
    node2 = Node(32)
    node3 = Node(17)
    node1.left = node2
    node1.right = node3
    bts = BinarySearchTree(node1)
    assert bts.contains(20) == False

def test_max():
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
    assert bt.max() == 32

def test_max_fail():
    node1 = Node(0)
    bt = BinaryTree(node1)
    node2 = Node(2)
    node3 = Node(7)
    node4 = Node(3)
    node5 = Node(10)
    node1.left = node2
    node1.left.left = node4
    node1.right = node3
    node1.right.right = node5
    assert bt.max() != 0