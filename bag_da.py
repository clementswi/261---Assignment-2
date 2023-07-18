# Name: William Clements
# OSU Email: clementswi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 7/18/2023
# Description: methods for a provided Bag ADT class


from dynamic_array import *
class Bag:
    def __init__(self, start_bag=None):
        """Init new bag based on Dynamic Array"""
        self._da = DynamicArray()
        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)
    def __str__(self) -> str:
        """Return content of stack in human-readable form"""
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
        for _ in range(self._da.length())])
        return out + ']'
    def size(self) -> int:
        """Return total number of items currently in the bag"""
        return self._da.length()


# -----------------------------------------------------------------------
    def add(self, value: object) -> None:
        """Add a new element to the bag."""
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """Remove any one element from the bag that matches the provided value object."""
        for element in range(self._da.length()):
            if self._da[element] == value:
                self._da.remove_at_index(element)
                return True
        return False

    def count(self, value: object) -> int:
        """Return the number of elements in the bag that match the provided value object."""
        count = 0
        for element in range(self._da.length()):
            if self._da[element] == value:
                count += 1
        return count

    def clear(self) -> None:
        """Clear the contents of the bag."""
        self._da = DynamicArray()  # Create a new empty dynamic array

    def equal(self, second_bag: "Bag") -> bool:
        """Check if the contents of two bags are equal."""
        # Step 1: Compare lengths of both bags
        if self._da.length() != second_bag._da.length():
            return False

        # Step 2: Check if all elements of self are in second_bag
        for num in range(self._da.length()):
            element = self._da.get_at_index(num)
            if second_bag._da.index_of(element) == -1:
                return False

        # Step 3: Check if all elements of second_bag are in self
        for num in range(second_bag._da.length()):
            element = second_bag._da.get_at_index(num)
            if self._da.index_of(element) == -1:
                return False

        # Step 4: All elements are found in both bags
        return True

    def __iter__(self):
        """Create iterator for the Bag"""
        index = 0
        while index < self._da.length():
            yield self._da.get_at_index(index)
            index += 1

    class BagIterator:
        def __init__(self, bag):
            self._bag = bag
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < self._bag.size():
                value = self._bag.get_at_index(self._index)
                self._index += 1
                return value
            raise StopIteration

    def __init__(self, start_bag=None):
        """Initialize a new bag based on Dynamic Array"""
        self._da = DynamicArray()
        # populate bag with initial values (if provided)
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """Return content of bag in human-readable form"""
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(i)) for i in range(self._da.length())])
        return out + ']'

    def add(self, value: object) -> None:
        """Add a new element to the bag"""
        self._da.append(value)

    def size(self) -> int:
        """Return total number of items currently in the bag"""
        return self._da.length()

    def __iter__(self):
        """Create iterator for the Bag"""
        return self.BagIterator(self)