from collections import deque


def main():
    # A list is identical to a vector where a new array is created when
    # there are too many elements and the old elements are moved over to
    # the new array one-by-one. The time complexity involved with growing
    # its size is linear. A deque is identical to a doubly linked list
    # whose nodes have a left pointer and a right pointer. In order to
    # grow the linked list, a new node is created and added to the left
    # or the right of the linked list. The time complexity involved with
    # growing its size is constant. Check out the source code for a list
    # and a deque to learn more:
    # https://github.com/python/cpython/blob/3.8/Objects/listobject.c
    # https://github.com/python/cpython/blob/3.8/Modules/_collectionsmodule.c
    dq = deque()

    for i in range(1, 5):
        # Similar to adding a new node to the right of the linked list
        dq.append(i)

        # Similar to adding a new node to the left of the linked list
        dq.appendleft(i * 2)

    # A deque can be iterated on to build a sequence of choice
    assert [el for el in dq] == [8, 6, 4, 2, 1, 2, 3, 4]
    assert tuple(el for el in dq) == (8, 6, 4, 2, 1, 2, 3, 4)

    # A deque can be used as a stack
    # https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    assert dq.pop() == 4
    assert dq.pop() == 3

    # A deque can be used as a queue
    # https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    assert dq.popleft() == 8
    assert dq.popleft() == 6


if __name__ == '__main__':
    main()
