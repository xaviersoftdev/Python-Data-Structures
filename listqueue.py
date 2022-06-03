"""
File: listqueue.py
Author: Man-Chi Leung
"""


class ListQueue(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.queue = []
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.queue)

    def __str__(self):
        """Returns the string representation of the queue."""
        return '{' + ', '.join((map(str, self))) + '}'

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        cursor = 0
        while cursor < len(self):
            yield self.queue[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        result = ListQueue(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        else:
            return False

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is empty."""
        if self.isEmpty():
            raise IndexError
        else:
            return self.queue[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.queue = []

    def add(self, item):
        """Inserts item at rear of the queue."""
        self.queue.append(item)

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is not empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise IndexError
        else:
            return self.queue.pop(0)
