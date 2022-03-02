from code_challenges.insertion_sort import insert_sort
from code_challenges.__init__ import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_inorder():
    arr = [1,2,5,9,12]
    insert_sort.insert_sort(arr)
    assert arr == [1,2,5,9,12]

def test_outorder():
    arr = [1,5,12,2,9]
    insert_sort.insert_sort(arr)
    assert arr == [1,2,5,9,12]

def test_single():
    arr = [5]
    insert_sort.insert_sort(arr)
    assert arr == [5]