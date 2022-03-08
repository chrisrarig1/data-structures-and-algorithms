from code_challenges.quick_sort import quick_sorted
from code_challenges.__init__ import __version__
import pytest

left = 0

def test_version():
    assert __version__ == '0.1.0'

def test_normal():
    arr = [8,4,23,42,16,15]
    right = len(arr)-1
    quick_sorted.quick_sort(arr,left,right)
    assert arr == [4,8,15,16,23,42]

def test_reverse():
    arr = [20,18,12,8,5,-2]
    right = len(arr)-1
    quick_sorted.quick_sort(arr,left,right)
    assert arr == [-2,5,8,12,18,20]

def test_unique():
    arr = [5,12,7,5,5,7]
    right = len(arr)-1
    quick_sorted.quick_sort(arr,left,right)
    assert arr == [5,5,5,7,7,12]

def test_nearly():
    arr = [2,3,5,7,13,11]
    right = len(arr)-1
    quick_sorted.quick_sort(arr,left,right)
    assert arr == [2,3,5,7,11,13]