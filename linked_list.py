"""
File: linked_list.py

Add an insert and a remove function.

Tests the Node class.
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe != None:
        count += 1
        probe = probe.next
    return count
    
def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""
    if index <= 0:
        # newItem goes at the head
        head = Node(newItem, head)
    else:
        # Search for node at position index - 1 or the last position
        probe = head
        while index > 1 and probe.next != None:   
            probe = probe.next
            index -= 1
        # Insert new node after node at position index - 1 
        # or last position
        probe.next = Node(newItem, probe.next)
    return head

def remove(index, head):
    """Removes the item at index from the linked structure
    referred to by head and returns the tuple (head, item)
    Precondition: 0 <= index < length(head)"""
    if index < 0 or index >= length(head):
        raise IndexError("Index out of bounds")
    # Assumes that the linked structure has at least one item
    if index == 0:
        removedItem = head.data
        head = head.next
    else:
        # Search for node at position index - 1 or 
        # the next to last position
        probe = head
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        removedItem = probe.next.data
        probe.next = probe.next.next
    return (head, removedItem)


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print(probe.data, end = " ")
        probe = probe.next
    print()


def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("Insert 1 at index 0:", end = " ")
    printStructure(head)

    head = insert(1, "2", head)
    print("Insert 2 at index 1:", end = " ")
    printStructure(head)

    head = insert(0, "0", head)
    print("Insert 0 at index 0:", end = " ")
    printStructure(head)

    head = insert(3, "3", head)
    print("Insert 3 at index 3:", end = " ")
    printStructure(head)

    head = insert(1, "9", head)
    print("Insert 9 at index 1:", end = " ")
    printStructure(head)


    (head, item) = remove(0, head)
    print("First element removed:", end = " ")
    printStructure(head)

    (head, item) = remove(0, head)
    print("First element removed:", end = " ")
    printStructure(head)
    
    (head, item) = remove(length(head) - 1, head)
    print("Last element removed:", end = " ")
    printStructure(head)

    (head, item) = remove(1, head)
    print("Second element removed:", end = " ")
    printStructure(head)

if __name__ == "__main__": main()


