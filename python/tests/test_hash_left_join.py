from code_challenges.hash_table.hash_table import HashTable, Node
from code_challenges.hash_left_join.left_join import left_join
import pytest


def test_hash_keys1():
    hash1 = HashTable()
    hash1.set('Hi','Hello')
    hash1.set('Dog', 'Good')
    hash2 = HashTable()
    hash2.set('Hi','Holla')
    hash2.set('Bye', 'Ciao')
    assert left_join(hash1,hash2) == ['Hi','Hello','Holla','Dog', 'Good', 'Null']

def test_hash_keys2():
    hash1 = HashTable()
    hash1.set('Hi','Hello')
    hash1.set('Dog', 'Good')
    hash1.set('Yes', 'Yup')
    hash2 = HashTable()
    hash2.set('Hi','Holla')
    hash2.set('Bye', 'Ciao')
    hash2.set('Yes', 'Ok')
    assert left_join(hash1,hash2) == ['Hi','Hello','Holla','Dog', 'Good', 'Null', 'Yes', 'Yup','Ok']

def test_hash_keys3():
    hash1 = HashTable()
    hash1.set('Hi','Hello')
    hash1.set('Dog', 'Good')
    hash1.set('Ok','Yup')
    hash1.set('Bye', 'Cya')
    hash2 = HashTable()
    hash2.set('Hi','Holla')
    hash2.set('Ok','Si')
    hash2.set('Bye', 'Ciao')
    hash2.set('No', 'Nope')
    assert left_join(hash1,hash2) == ['Hi','Hello','Holla','Dog','Good','Null','Bye', 'Cya','Ciao','Ok','Yup','Si']


