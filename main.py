# Name:William Clements
# OSU Email:clementsw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:1, Part 1
# Due Date:7/11/23
# Description:Various methods such as sort and min max for a given static array class



from static_array import StaticArray



def resize(self, new_capacity: int) -> None:
    if new_capacity <= 0 or new_capacity < self._size:
        return

    new_data = StaticArray(new_capacity)
    for element in range(self._size):
        new_data.set(element, self._data.get(element))

    self._data = new_data

def append(self, value: object) -> None:
    """Add a new value at the end of the dynamic array.

    Args:
        value (object): The value to be appended to the dynamic array.

    Notes:
        If the internal storage associated with the dynamic array is already full,
        the capacity will be doubled using the `resize` method before adding the new value.
        """

    if self._size == self._data.get_length():
        self.resize(2 * self._data.get_length())

    self._data.set(self._size, value)
    self._size += 1

def insert_at_index(self, index: int, value: object) -> None:
    """Add a new value at the specified index in the dynamic array.

    Args:
        index (int): The index at which the value will be inserted.
        value (object): The value to be inserted into the dynamic array.

    Raises:
        DynamicArrayException: If the provided index is invalid.

    Returns:
        None.
        """
    if index < 0 or index > self._size:
        raise DynamicArrayException("Invalid index")

    if self._size == self._data.get_length():
        self.resize(2 * self._data.get_length())

    for element in range(self._size, index, -1):
        self._data.set(i, self._data.get(i - 1))

    self._data.set(index, value)
    self._size += 1

def remove_at_index(self, index: int) -> None:
    """Remove the element at the specified index in the dynamic array.

    Args:
        index (int): The index of the element to be removed.

    Raises:
        DynamicArrayException: If the provided index is invalid.

    Returns:
        None.
        """
    if index < 0 or index >= self._size:
        raise DynamicArrayException("Invalid index")

    for element in range(index, self._size - 1):
        self._data.set(element, self._data.get(element + 1))

    self._data.set(self._size - 1, None)
    self._size -= 1

    # Reduce capacity if needed
    if self._size < self._data.get_length() // 4 and self._data.get_length() > 10:
        new_capacity = max(self._size * 2, 10)
        self.resize(new_capacity)

def slice(self, start_index: int, size: int) -> object:
    """Return a new DynamicArray object that contains the requested elements from the original array.

    Args:
        start_index (int): The index of the first element to include in the slice.
        size (int): The number of elements to include in the slice.

    Raises:
        DynamicArrayException: If the provided start index or size is invalid,
            or if there are not enough elements to make the slice of the requested size.

    Returns:
        DynamicArray: A new DynamicArray object representing the slice.
        """
    if start_index < 0 or start_index >= self._size or size < 0 or start_index + size > self._size:
        raise DynamicArrayException("Invalid start index or size")

    new_da = DynamicArray()
    for element in range(start_index, start_index + size):
        new_da.append(self._data.get(element))

    return new_da

def merge(self, second_da: object) -> None:
    """Append all elements from the input DynamicArray object onto the current one.

    Args:
        second_da (DynamicArray): The DynamicArray object whose elements will be appended.

    Note:
        The elements from the input DynamicArray are appended to the end of the current one,
        in the same order in which they are stored in the input array."""

    for element in range(second_da.length()):
        self.append(second_da._data.get(element))


def map(self, map_func) -> object:
    """Create a new DynamicArray object where each element is derived by applying a given map_func to the original array.

    Args:
        map_func (function): The function to be applied to each element.

    Returns:
        DynamicArray: A new DynamicArray object containing the mapped values.
        """
    new_da = DynamicArray()
    for element in range(self._size):
        new_da.append(map_func(self._data.get(element)))
    return new_da

def filter(self, filter_func) -> object:
    """Create a new DynamicArray object populated only with elements for which filter_func returns True.

    Args:
        filter_func (function): The filter function to be applied.

    Returns:
        DynamicArray: A new DynamicArray object containing the filtered elements.
        """
    new_da = DynamicArray()
    for element in range(self._size):
        if filter_func(self._data.get(element)):
            new_da.append(self._data.get(element))
    return new_da

def reduce(self, reduce_func, initializer=None) -> object:
    """Sequentially applies the reduce_func to all elements of the dynamic array and returns the resulting value.

    Args:
        reduce_func (function): The reduce function to be applied.
        initializer (optional): The initial value for the reduction. Defaults to None.

    Returns:
        object: The result of the reduction.
        """
    if self._size == 0:
        return initializer

    if initializer is None:
        accumulator = self._data.get(0)
        start_index = 1
    else:
        accumulator = initializer
        start_index = 0

    for element in range(start_index, self._size):
        accumulator = reduce_func(accumulator, self._data.get(element))

    return accumulator


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """Find the mode(s) and frequency of occurrence in a sorted DynamicArray"""
    if arr.is_empty():
        return DynamicArray(), 0

    mode = DynamicArray()
    max_freq = 0
    current_freq = 1

    for element in range(1, arr.length()):
        if arr[element] == arr[element - 1]:
            current_freq += 1
        else:
            if current_freq > max_freq:
                max_freq = current_freq
                mode = DynamicArray([arr[element - 1]])
            elif current_freq == max_freq:
                mode.append(arr[element - 1])
            current_freq = 1

    # Check the last element
    if current_freq > max_freq:
        mode = DynamicArray([arr[-1]])
    elif current_freq == max_freq:
        mode.append(arr[-1])

    return mode, max_freq
