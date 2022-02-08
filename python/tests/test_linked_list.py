from linked_list.linked_list import Node, LinkedList
import pytest

# Can successfully instantiate an empty linked list
def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None
# Can properly insert into the linked list
def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_insert_to_empty_linked_list():
    # ll.head = apple
    ll = LinkedList()
    ll.insert('fish')
    assert ll.head.value != 'turtle'
# The head property will properly point to the first node in the linked list
def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

def test_notlinked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head != 2


# Can properly insert multiple nodes into the linked list
def test_insert_multiple():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    ll.insert(5)
    assert ll.head.value == 5
    ll.insert(7)
    assert ll.head.value == 7
# Will return true when finding a value within the linked list that exists
def test_find_value():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.includes(3) == True 
# Will return false when searching for a value in the linked list that does not exist
def test_notfind_value():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.includes(8) != True 

# Can properly return a collection of all the values that exist in the linked list
def test_string_value():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.__str__()== '{3} -> {6} -> {7} -> {5} -> NULL'

def test_notstring_value():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.__str__()!= '{3} -> {7} -> {5} -> NULL'

# Code Challenge 06
# Can successfully add a node to the end of the linked list
@pytest.mark.skip
def test_append():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    assert ll.append(2) == 2 

# Can successfully add multiple nodes to the end of a linked list
@pytest.mark.skip
def test_multiappend():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    assert node2.next == None
    ll.append(2)
    assert node2.next == 2 
# Can successfully insert a node before a node located i the middle of a linked list
@pytest.mark.skip
def test_insert_before():
    ll= LinkedList()
    ll.insert(5)
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    ll.insert_after(1,2)
    assert node1.next == 2
# Can successfully insert a node before the first node of a linked list
@pytest.mark.skip
def test_insert_before():
    ll= LinkedList()
    ll.insert(5)
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    ll.insert_after(1,2)
    assert node1.next == 2
# Can successfully insert after a node in the middle of the linked list
@pytest.mark.skip
def test_insert_after():
    ll= LinkedList()
    ll.insert(5)
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    ll.insert_after(1,2)
    assert node1.next == 2
# Can successfully insert a node after the last node of the linked list
@pytest.mark.skip
def test_insert_last():
    ll= LinkedList()
    ll.insert(5)
    node1 = Node(1)
    node2 = Node(3)
    node1.next = node2
    assert ll.insert_after(1,2) == 2


# Code Challenge 07
# Where k is greater than the length of the linked list
def test_greater_than_length():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.kth_from_end(5) == 'Exception'

# Where k and the length of the list are the same
def test_equal_length():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.kth_from_end(4) == 3
# Where k is not a positive integer
def test_not_positive():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    assert ll.kth_from_end(-1) == 'Exception'
# Where the linked list is of a size 1
def test_one_size():
    ll = LinkedList()
    ll.insert(5)
    assert ll.kth_from_end(1) == 5
# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_middle_val():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(10)
    ll.insert(6)
    ll.insert(3)
    assert ll.kth_from_end(3) == 10

def test_zip_list():
    l2 = LinkedList()
    ll = LinkedList()
    l2.insert(15)
    l2.insert(17)
    l2.insert(16)
    l2.insert(13)
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    new = ll.zip_lists(ll,l2)
    newlist = new.__str__()
    expected = '{3} -> {13} -> {6} -> {16} -> {7} -> {17} -> {5} -> {15} -> NULL'
    assert newlist == expected

def test_shortzip_list():
    l2 = LinkedList()
    ll = LinkedList()
    l2.insert(15)
    l2.insert(17)
    l2.insert(16)
    ll.insert(5)
    ll.insert(7)
    ll.insert(6)
    ll.insert(3)
    new = ll.zip_lists(ll,l2)
    newlist = new.__str__()
    expected = '{3} -> {16} -> {6} -> {17} -> {7} -> {15} -> {5} -> NULL'
    assert newlist == expected

def test_greater_than_length():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)
    newlist = ll.__str__()
    print (newlist)
    assert ll.order() == True


