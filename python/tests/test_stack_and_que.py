from code_challenges.stack_and_queue.queue import Queue
from code_challenges.stack_and_queue.stack import Stack
from code_challenges.stack_and_queue.stack_queue_pseudo import PseudoQueue
from code_challenges.stack_and_queue.stack_queue_animal_shelter import AnimalShelter
from code_challenges.stack_and_queue.stack_queue_brackets import Brackets
import pytest

# Can successfully push onto a stack
def test_push():
    new_stack = Stack()
    new_stack.push(4)
    assert new_stack.top.value == 4
# Can successfully push multiple values onto a stack
def test_push_multi():
    new_stack = Stack()
    new_stack.push(4)
    assert new_stack.top.value == 4
    new_stack.push(6)
    assert new_stack.top.value == 6
    new_stack.push(9)
    assert new_stack.top.value == 9
# Can successfully pop off the stack
def test_pop():
    new_stack = Stack()
    new_stack.push(4)
    new_stack.push(6)
    new_stack.push(9)
    new_stack.pop()
    assert new_stack.top.value == 6
# Can successfully empty a stack after multiple pops
def test_pop_multi():
    new_stack = Stack()
    new_stack.push(4)
    new_stack.push(6)
    new_stack.push(9)
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    assert new_stack.top == None
# Can successfully peek the next item on the stack
def test_peek():
    new_stack = Stack()
    new_stack.push(4)
    new_stack.push(6)
    new_stack.push(9)
    assert new_stack.peek() == 9
# Can successfully instantiate an empty stack
def test_empty():
    new_stack = Stack()
    assert new_stack.empty() == True
# Calling pop or peek on empty stack raises exception
def test_peek_pop():
    new_stack = Stack()
    assert new_stack.pop() == "empty stack"
    assert new_stack.peek() == "empty stack"
# Can successfully enqueue into a queue
def test_enqueue():
    new_que = Queue()
    new_que.enqueue(8)
    assert new_que.rear.value == 8
# Can successfully enqueue multiple values into a queue
def test_multi_enqueue():
    new_que = Queue()
    new_que.enqueue(8)
    new_que.enqueue(9)
    new_que.enqueue(10)
    assert new_que.rear.value == 10
# Can successfully dequeue out of a queue the expected value
def test_deq():
    new_que = Queue()
    new_que.enqueue(8)
    new_que.enqueue(9)
    new_que.enqueue(10)
    new_que.dequeue()
    assert new_que.front.value == 9
# Can successfully peek into a queue, seeing the expected value
def test_peek_que():
    new_que = Queue()
    new_que.enqueue(8)
    new_que.enqueue(9)
    new_que.enqueue(10)
    new_que.peek()
    assert new_que.peek() == 8

# Can successfully empty a queue after multiple dequeues
def test_deq_empty():
    new_que = Queue()
    new_que.enqueue(8)
    new_que.enqueue(9)
    new_que.enqueue(10)
    new_que.dequeue()
    new_que.dequeue()
    new_que.dequeue()
    assert new_que.front == None
# Can successfully instantiate an empty queue
def test_que_empty():
    new_que = Queue()
    assert new_que.isempty() == True
# Calling dequeue or peek on empty queue raises exception
def test_peek_deq():
    new_que = Queue()
    assert new_que.dequeue() == "empty que"
    assert new_que.peek() == "empty que"



# Pseudo Tests
def test_psuedo_empty():
    new_stacks = PseudoQueue()
    assert new_stacks.stack2.peek() == "empty stack"
    assert new_stacks.stack1.peek() == "empty stack"


def test_psuedo_enq():
    new_stacks = PseudoQueue()
    new_stacks.enqueue(4)
    assert new_stacks.stack2.top.value == 4
    new_stacks.enqueue(7)
    new_stacks.enqueue(6)
    assert new_stacks.stack2.top.value == 6
    new_stacks.enqueue(9)

def test_psuedo_deq():
    new_stacks = PseudoQueue()
    new_stacks.enqueue(4)
    new_stacks.enqueue(7)
    new_stacks.enqueue(6)
    new_stacks.enqueue(9)
    assert new_stacks.dequeue() == 9
    assert new_stacks.stack2.top.value == 6

def test_psuedo_deq_err():
    new_stacks = PseudoQueue()
    new_stacks.enqueue(4)
    new_stacks.enqueue(7)
    new_stacks.enqueue(6)
    new_stacks.enqueue(9)
    new_stacks.dequeue()
    new_stacks.dequeue()
    new_stacks.dequeue()
    new_stacks.dequeue()
    assert new_stacks.dequeue() == 'empty stack'

# Animal Shelter tests:
def test_animal_null():
    new_que = AnimalShelter()
    assert new_que.enqueue('rat') == 'Null'

def test_animal_null2():
    new_que = AnimalShelter()
    assert new_que.dequeue('rat') == 'Null'

def test_animal_enq():
    new_que = AnimalShelter()
    new_que.enqueue('dog')
    new_que.enqueue('dog')
    new_que.enqueue('cat')
    assert new_que.rear.value == 'cat'

def test_animal_deq():
    new_que = AnimalShelter()
    new_que.enqueue('dog')
    new_que.enqueue('cat')
    new_que.enqueue('dog')
    new_que.enqueue('dog')
    new_que.enqueue('cat')
    assert new_que.dequeue('cat') == 'cat'

def test_animal_queue():
    new_que = AnimalShelter()
    new_que.enqueue('dog')
    new_que.enqueue('cat')
    new_que.enqueue('dog')
    new_que.enqueue('dog')
    new_que.enqueue('cat')
    new_que.dequeue('cat')
    assert  new_que.rear.value == 'cat'

# Bracket Validation Tests

def test_brackets():
    bv = Brackets()
    assert  bv.validate_brackets('[]') == True

def test_brackets2():
    bv = Brackets()
    assert  bv.validate_brackets('[]()') == True

def test_multi_brackets():
    bv = Brackets()
    assert  bv.validate_brackets('({}[][])') == True

def test_fail_brackets():
    bv = Brackets()
    assert  bv.validate_brackets('({}[][]') == False



def test_fail_brackets2():
    bv = Brackets()
    assert  bv.validate_brackets('[{{}]') == False

def test_words_brackets():
    bv = Brackets()
    assert  bv.validate_brackets('{}{Code}[Fellows](())') == True