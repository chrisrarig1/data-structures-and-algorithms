from hash_table.hash_table import HashTable, Node
import pytest

def test_hash_node():
    node = Node('Cat',28)
    actualkey = node.key
    expectedkey = 'Cat'
    actualvalue = node.value
    expectedvalue = 28
    assert actualkey == expectedkey
    assert actualvalue == expectedvalue

def test_hash_table():
    hash = HashTable(4)
    actualsize = hash.size
    expectedsize = 4
    assert actualsize == expectedsize
    assert hash.bucket == [None,None,None,None]

def test_hash_set():
    hash = HashTable()
    hash.set('Cat',28)
    assert hash.hash('Cat') == 136
    assert hash.bucket[136].value == 28
    assert hash.bucket[136].key == 'Cat'

def test_hash_get():
    hash = HashTable()
    hash.set('Cat',28)
    hash.set('Dog', 55)
    assert hash.get('Cat') == 28
    assert hash.get('Dog') == 55

def test_hash_contains():
    hash = HashTable()
    hash.set('Cat',28)
    hash.set('Dog', 55)
    assert hash.contains('Cat') == True
    assert hash.contains('Apple') == False

def test_hash_keys():
    hash = HashTable()
    hash.set('Cat',28)
    hash.set('Dog', 55)
    hash.set('Pat',36)
    hash.set('Hog', 15)
    assert hash.keys() ==['Cat','Dog','Hog','Pat']

