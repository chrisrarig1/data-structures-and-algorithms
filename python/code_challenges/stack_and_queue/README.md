# Stacks and Queues

- Create a Stack class that has a top property.
  - The class should contain the following methods:
    1. Push
    2. Pop
    3. Peek
    4. Empty
- Create a Queue class that has a front property. 
  - The class should contain the following methods:
    1. Enqueue
    2. Dequeue
    3. Peek
    4. Empty

## Challenge

- Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency

- My approach to this was a test development approach.
- The functions themselves are all O(1)

## API

- Push:
  - Adds a new node with that value to the top of the stack with an O(1) Time performance.

- Pop:
  - Removes the node from the top of the stack.

- Peek:
  - Returns: Value of the node located at the top of the stack

- Empty:
  - Returns: Boolean indicating whether or not the stack is empty.

- Enqueue:
  - adds a new node with that value to the back of the queue with an O(1) Time performance.

- Dequeue:
  - Removes the node from the front of the queue

- Peek:
  - Returns: Value of the node located at the top of the stack

- Empty:
  - Returns: Boolean indicating whether or not the stack is empty.

- [PR]: (https://github.com/chrisrarig1/data-structures-and-algorithms/pull/26)


# Pseudo Queue

- Create a new class called pseudo queue.
  - Utilize 2 Stack instances to create and manage the queue
    1. Enqueue
    2. Dequeue

## Approach & Efficiency

- My approach to this was a test development approach.

## API

- Enqueue:
  - Inserts value into the PseudoQueue, using a first-in, first-out approach.
- Dequeue:
  - Extracts a value from the PseudoQueue, using a first-in, first-out approach

- [PR]: (https://github.com/chrisrarig1/data-structures-and-algorithms/pull/27)

# Animal Shelter

## Challenge Summary

- Create a class called AnimalShelter which holds only dogs and cats.
- The shelter operates using a first-in, first-out approach.
- Implement the following methods:
  1. Enqueue
  2. Dequeue

## Whiteboard Process
[White board](Animal.png)

## Approach & Efficiency

- I took a test development approach on this one. I took a look at the behavior between a Stack and a Queue and used that to manipulate the return Queue

## Solution

- The code takes in a preference ("cat" or "dog"). It then traverses through the Queue to see if the front value matches the preference. If it does not that value is then pushed into a stack if it does match it returns it. I then took that stack and traversed through that and popped and pushed its values into another stack then took that stack and popped and enqueued its values back into the Queue.

- [PR]: (https://github.com/chrisrarig1/data-structures-and-algorithms/pull/28)

# Bracket Check

## Challenge Summary

- Create a function that takes in a string and verifies whether or not any brackets are complete

## Whiteboard Process
[White board](CodeChallenge13.png)

## Approach & Efficiency

- I took a test development approach on this one. I took a look at the behavior between a Stack and a Queue and used that to manipulate the return Queue

## Solution

- Used Stack method to check whether or not opening bracket had a closing bracket. This was done by pushing the opening brackets into a stack then using a dictionary to see if the next value matches the opening bracket. If it does the stack item is then popped. Once all the items are out of the stack return true

- [PR]: (https://github.com/chrisrarig1/data-structures-and-algorithms/pull/30)