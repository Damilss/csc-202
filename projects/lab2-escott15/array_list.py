from dataclasses import dataclass

from typing import Any


@dataclass
class ArrayList:
    array: list[Any]
    capacity: int
    size: int


# NOTE: Initial capacity for an empty list is somewhat arbitrary.  To
# making testing resizing easier, you'll probably want a small initial
# capacity (so I'm using 1 here).  In practice, you'd probably have an
# initial capacity of 5–10.
def empty_list() -> ArrayList:
    return ArrayList([None], 1, 0)


def add_item(lst: ArrayList, idx: int, value: Any) -> None:
    """Takes a list, an integer index,
    and another value (of any type), as arguments and places the value at
    whatever given index. if Index is invalid, raise IndexError. 
    :param lst: Description
    :type lst: ArrayList
    :param index: Description
    :type index: int
    :param value: Description
    :type value: Any
    """
    if idx > lst.size or idx < 0: 
        raise IndexError
    
    if lst.size + 1 > lst.capacity:
        lst.capacity *= 2
        for i in (lst.capacity - len(lst.array)):
            lst.array += [None] 
        
    small_idx = lst.size
    while small_idx >= idx: 
        if small_idx == idx:
            lst.array[idx] = value 
        else: 
            lst.array[small_idx] = lst.array[small_idx-1]
        small_idx -=1    
    lst.size +=1 


def length(lst: ArrayList) -> int:
    """Returns length of ArrayList.
    :param lst: Description
    :type lst: ArrayList
    :return: Description
    :rtype: int"""
    return lst.size


def get_item(lst: ArrayList, idx: int) -> Any:
    """Takes an int as an index and returns that value at index position
    :param lst: Description
    :type lst: ArrayList
    :param index: Description
    :type index: int
    :return: Description
    :rtype: Any"""
    if idx >= lst.size or idx < 0: 
        raise IndexError
    return lst.array[idx]


def set_item(lst: ArrayList, idx: int, value: Any) -> None:
    """Takes list, int and another value as args and returns the value at the
    index position in the list. 
    :param lst: Description
    :type lst: ArrayList
    :param index: Description
    :type index: int
    :param value: Description
    :ype value: Any"""
    if idx >= lst.size: 
        raise IndexError
    lst.array[idx] = value


def remove(lst: ArrayList, idx: int) -> Any:
    """Removes Array list at given list
    :param lst: Description
    :type lst: ArrayList
    :param index: Description
    :type index: int
    :return: Description
    :rtype: Any"""
    if idx >= lst.size: 
        raise IndexError
    
    result = lst.array[idx]
    end = lst.array[idx + 1:]
    lst.array = lst.array[:idx]
    lst.array.extend(end)
    lst.size -= 1
    return result 