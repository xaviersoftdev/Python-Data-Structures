"""
File: listbag.py
Author: Man-Chi Leung
"""

from listbag import ListBag


class ListSortedBag(ListBag):
    """An list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ListBag.__init__(self, sourceCollection)

    # Accessor methods

    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise.
        Use binary search"""

        visited = []
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            visited.append(self.items[midPoint])
            if self.items[midPoint] == item:
                print("Items visited:", visited)
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        print("Items visited:", visited)
        return False

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""

        result = ListSortedBag(self)
        for item in other:
            result.add(item)
        return result

    # Mutator methods
    def add(self, item):
        """Adds item to self."""

        if self.isEmpty():
            self.items.append(item)
            print("Item added:", item, "  Item added at front")
        elif item >= self.items[-1]:
            self.items.append(item)
            print("Item added:", item, "  Item added at back end")
        else:
            visited = []
            # Search for first item >= new item
            targetIndex = 0
            while item > self.items[targetIndex]:
                visited.append(self.items[targetIndex])
                targetIndex += 1
            visited.append(self.items[targetIndex])
            print("Item added:", item, "  Items visited:", visited)

            # Insert item and update size
            self.items.insert(targetIndex, item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""

        # Check precondition and raise KeyError if necessary
        if item not in self:
            raise KeyError("Item not in bag")
        else:
            visited = []
            # Search for first item == new item
            targetIndex = 0
            while item > self.items[targetIndex]:
                visited.append(self.items[targetIndex])
                targetIndex += 1
            visited.append(self.items[targetIndex])
            print("Item removed", item, "  Items visited:", visited)

            # Insert item and update size
            del self.items[targetIndex]
