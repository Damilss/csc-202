from dataclasses import dataclass

from collections.abc import Iterator
from typing import Any

type BST = TreeNode | None


@dataclass(frozen=True)
class TreeNode:
    value: Any
    left: BST
    right: BST


def is_empty(tree: BST) -> bool:
    """Return True if the tree is empty, False otherwise."""
    if tree is None: 
        return True
     
    return False 


def search(tree: BST, value: Any) -> bool:
    """Return True if value is in tree, False otherwise."""
    if is_empty(tree):
        return False
    elif tree.value == value:
        return True
    elif search(tree.left, value):
        return True
    elif search(tree.right, value):
        return True
    
    return False


def insert(tree: BST, value: Any) -> BST:
    """Insert the value into the tree in the proper location."""
    if tree is None:
        return TreeNode(value, None, None)
    
    if value < tree.value:
        return TreeNode( 
            tree.value,
            insert(tree.left, value),
            tree.right
        )
    
    if value > tree.value: 
        return TreeNode(
            tree.value, 
            tree.left, 
            insert(tree.right, value)
        )
    
    return tree


def delete(tree: BST, value: Any) -> BST:
    """Remove the value from the tree (if present).

    If the value is not present, this function does nothing.
    """
    if tree is None: 
        return
    
    if value > tree.value:
        return TreeNode(
            tree.value,
            tree.left,
            delete(tree.right, value)
        )
    
    if value < tree.value:
        return TreeNode(
            tree.value,
            delete(tree.left, value),
            tree.right
        )
    
    if tree.left is None and tree.right is None: 
        return 
    
    if tree.left is None: 
        return tree.right
    
    if tree.right is None: 
        return tree.left
    
    next_value = find_min(tree.right)

    return TreeNode(
        next_value, 
        tree.left, 
        delete(tree.right, next_value)
    )


def find_min(tree: BST) -> Any:
    """Return the smallest value in the tree."""
    if tree is None:
        return
        
    if tree.left is None: 
        return tree.value

    return find_min(tree.left)


def find_max(tree: BST) -> Any:
    """Return the largest value in the tree."""
    if tree is None: 
        return
    
    if tree.right is None:
        return tree.value
    
    return find_max(tree.right)    


def height(tree: BST) -> int:
    """Return the height of the tree."""
    if tree is None:
        return -1
    
    left_height = height(tree.left)
    right_height = height(tree.right)

    if left_height > right_height: 
        return 1 + left_height
    else: 
        return 1 + right_height


def prefix_iterator(tree: BST) -> Iterator[Any]:
    """Return an iterator over the tree in prefix order."""
    if tree is None: 
        return 
    
    yield tree.value 
    yield from prefix_iterator(tree.left)
    yield from prefix_iterator(tree.right)


def infix_iterator(tree: BST) -> Iterator[Any]:
    """Return an iterator over the tree in infix order."""
    if tree is None: 
        return
    
    yield from infix_iterator(tree.left)
    yield tree.value
    yield from infix_iterator(tree.right)


def postfix_iterator(tree: BST) -> Iterator[Any]:
    """Return an iterator over the tree in postfix order."""
    if tree is None: 
        return
    
    yield from postfix_iterator(tree.left)
    yield from postfix_iterator(tree.right)
    yield tree.value
