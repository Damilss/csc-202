from dataclasses import dataclass

from collections.abc import Callable
from typing import Any

# HashEntry is the type of a single key-value pair.
type HashEntry = tuple[Any, Any]
# HashChain is the type for the chains of the hash table.
type HashChain = list[HashEntry]

# NOTE: READ THE GIVEN TEST FIRST.  Before you write any code, you need
# to have a solid understanding of what each function is doing and why.


@dataclass
class HashTable:
    table: list[HashChain]
    capacity: int
    size: int
    hash_function: Callable[[Any], int]


# NOTE: Don't change this function.
def empty_table(hash_function: Callable[[Any], int]) -> HashTable:
    initial_capacity = 5

    return HashTable(
        [[] for _ in range(initial_capacity)],
        initial_capacity,
        0,
        hash_function,
    )


def set_item(hash_table: HashTable, key: Any, value: Any) -> None:
    """Function will take a hash table, a key, and a value as args. The
    function will insert the key-value pair into the hash table based
    on the hash value of the key mod the table size"""
    load_factor: float = (hash_table.size + 1) / hash_table.capacity

    new_entry_idx: int = hash_table.hash_function(key) % hash_table.capacity
    new_entry_chain: HashChain = hash_table.table[new_entry_idx]

    for idx, (k, v) in enumerate(new_entry_chain):
        if k == key: 
            new_entry_chain[idx] = (key, value)
            return  

    if load_factor > 1: 
        old_table = hash_table
        new_capacity = old_table.capacity * 2 
        new_table: list[HashChain] = [[] for _ in range(new_capacity)]

        for chain in old_table.table: 
            for (k, v) in chain: 
                new_idx = hash_table.hash_function(k) % new_capacity
                new_table[new_idx].append((k, v))

        hash_table.table = new_table
        hash_table.capacity = new_capacity

        new_entry_idx: int = hash_table.hash_function(key) % new_capacity
        new_entry_chain: HashChain = hash_table.table[new_entry_idx]

    new_entry_chain.append((key, value))
    hash_table.size += 1     


def get_item(hash_table: HashTable, key: Any) -> Any:
    """This function takes a hash table and a key as arguments. The function
    will retrieve the value for the given key,
    and will return the value"""

    idx: int = hash_table.hash_function(key) % hash_table.capacity
    chain: HashChain = hash_table.table[idx]
    
    for (k, value) in chain: 
        if key == k:
            return value 

    raise KeyError


def contains(hash_table: HashTable, key: Any) -> bool:
    """The function takes a hash table and a key as arguments. The function
    will remove the key-value pair from the hash table and return the value"""

    idx: int = hash_table.hash_function(key) % hash_table.capacity
    chain: HashChain = hash_table.table[idx]

    for k, value in chain: 
        if k == key: 
            return True
        
    return False


def remove(hash_table: HashTable, key: Any) -> Any:
    """Function takes a hash table and key as arguments.
    The function will remove the key value pair from the
    hash table and return the value.If key isn't present,
    the function will raise a KeyError."""

    chain_idx = hash_table.hash_function(key) % hash_table.capacity 
    entry_chain: HashChain = hash_table.table[chain_idx]

    for idx, (k, v) in enumerate(entry_chain):
        if k == key: 
            result = v 
            entry_chain.pop(idx)
            hash_table.size -= 1
            
            return result
        
    raise KeyError


def size(hash_table: HashTable) -> int:
    """function takes HashTable as argument and returnsthe
    number of key-value pairs that have been inserted into the hash table"""
    return hash_table.size


def keys(hash_table: HashTable) -> list[Any]:
    """This function takes a HashTable and returns a list of all
    of the keys in the table"""
    result = []

    for i in hash_table.table: 
        for (k, v) in i: 
            result.append(k)

    return result


def values(hash_table: HashTable) -> list[Any]:
    """this function takesa. has table as an argument and returns the
    key-value paris that have been inserted into the hash table"""
    result = [] 

    for i in hash_table.table:
        for (k, v) in i: 
            result.append(v)

    return result


def _contents(hash_table: HashTable) -> list[HashChain]:
    """This function takes a hash table as an argument and returns
    the internal hash table array. You may find this useful for testing"""
    return hash_table.table 


def djbx33a(s: str) -> int:
    """solve the djbx33a hash of a string."""
    h = 5381
    for ch in s:
        h = h * 33 + ord(ch)
    return h