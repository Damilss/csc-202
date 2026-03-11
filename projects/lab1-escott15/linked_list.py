"""Docstring for linked_list
Functions to create: 
    Empty_list: 
        This function takes no arguments and retuns empty lists 
    
    add_item: 
       This function takes a list, an integer index, and another value 
       (of any type) as arguments and inserts the value at index 
       position in the list (zero-based indexing; any element
        at the given index before this operation will now immediately
        follow the new element). If the index is invalid (i.e., less 
        than 0 or greater than the current length), then this 
        operation should raise an IndexError. (Note thatan 
        index equal to the length is allowed and results in 
        the new value being added to the end of the list.)
        This function must return the resulting list.
    
    length:
        This functions returns the number of elements currently in the list.

    get_item: 
        This function takes a list and an integer index as arguments and  
        returns the value at the index position in the list (zero-based 
        indexing). If the index is invalid (i.e., it falls outside the bounds
        of the list), then this operation should raise an IndexError

    set_item: 
        This function takes a list, an integer index, and another value 
        (of any type) as arguments and replaces the element at index 
        position in the list with the given value. If the index is invalid,
        then this operation should raise an IndexError.

    remove: 
        This function takes a list and an integer index as arguments and 
        removes the element at the index position from the list. 
        If the index is invalid (i.e., it falls outside the bounds of 
        the list), then this operation should raise an IndexError.
        This function must return a 2-tuple of, in this order, the 
        element previously at the specified index (i.e., the removed element)
        and the resulting list
        
    Testing: 
        Then go through and test the functions as many times as needed"""

from dataclasses import dataclass
from typing import Any

#defines what `LinkedList` is without actually setting it to anything. 
type LinkedList = Node | None


@dataclass(frozen=True)
class Node:
    """Docstring for Node:
    formated Node(first: any, rest: LinkedListr),
    where LinkedList is Node | None."""
    first: Any
    rest: LinkedList


def empty_list() -> LinkedList: #checked
    """ Docstring for empty_list: Returns an empty LinkedList,
    (which is None) and takes no arguments
    :return: Description
    :rtype: LinkedList """
    return None


def add_item(lst: LinkedList, idx: int, value: Any) -> LinkedList: # checked
    """Docstring for add_item: takes list, an integer (which is the index,
    and value of any type as arguments, and inserts value: Any, if index
    is invalid, raise IndexError. 
    :param lst: Description
    :type lst: LinkedList
    :param index: Description
    :type index: int
    :param value: Description
    :type value: Any
    :return: Description
    :rtype: LinkedList"""
    if lst is None and idx == 0: 
        return Node(value, None)
    elif lst is None and idx !=0 or idx < 0: 
        raise IndexError(
            "LinkedList out of range:" \
            "Please double check your given linked list and your given index"
        )
    elif lst is not None and idx == 0: 
        return Node(value, lst)
    elif lst is not None and idx !=0: 
        return Node(lst.first, add_item(lst.rest, idx - 1, value))  

def length(lst: LinkedList, idx: int = 0) -> int: #checked
    """ Docstring for length: 
    Returns the length of numnber of elements currently in a LinkedList 
    :param lst: Description
    :type lst: LinkedList
    :return: Description
    :rtype: int """
    if lst is None: 
        return idx 
    else: # lst is LinkedList
        return length(lst.rest, idx+1)
    


def get_item(lst: LinkedList, idx: int) -> Any:# checked
    """ Docstring for get_item:
    takes LinkedList and an int as args 
    and returns the element at that given index.
    :param lst: Description
    :type lst: LinkedList
    :param idx: Description
    :type idx: int
    :return: Description
    :rtype: Any """
    if lst is None and idx == 0: 
        return None
    elif lst is None and idx !=0 or idx < 0: 
        raise IndexError(
            "Linked list out of range of idx, plesae check your given list." \
            "and your index. "
        )
    elif lst is not None and idx == 0:
        return lst.first
    elif lst is not None and idx != 0: 
        return get_item(lst.rest, idx-1)
    
def set_item(lst: LinkedList, idx: int, value: Any) -> LinkedList: #checked
    """ Docstring for set_item: Function gets item at a specific index
    in a linked list, then replaces the element and any given index.
    :param lst: Description
    :type lst: LinkedList
    :param idx: Description
    :type idx: int
    :param value: Description
    :type value: Any
    :return: Description
    :rtype: LinkedList """
    if lst is None and idx == 0: 
        return Node(value, None) 
    if lst is None and idx != 0 or idx < 0: 
        raise IndexError(
            "Linked list is out of range:" \
            " Please double check your `idx`and your lst."
        )
    if lst is not None and idx == 0: 
        return Node(value, lst.rest)
    if lst is not None and idx !=0: 
        return Node(lst.first, set_item(lst.rest, idx-1, value))
    
    
def remove(lst: LinkedList, idx: int) -> tuple[Any, LinkedList]: #checked
    """ Docstring for remove: remove any given element within the
     given linked list. 
    :param lst: Description
    :type lst: LinkedList
    :param index: Description
    :type index: int
    :return: Description
    :rtype: tuple[Any, LinkedList] """
    if lst is None and idx != 0 or idx < 0: 
        raise IndexError(
            "Index for given Linked List out of range " \
            "please check your given list and given index."
        )
    elif lst is None and idx == 0: 
        return None, None
    elif lst is not None and idx != 0: 
        return remove(lst.rest, idx-1)
    elif lst is not None and idx == 0: 
        return lst.first, lst.rest