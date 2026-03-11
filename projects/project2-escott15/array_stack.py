from dataclasses import dataclass

from typing import Any


@dataclass
class ArrayStack:
    array: list[Any]
    capacity: int
    size: int


def empty_stack() -> ArrayStack:
    """creates and returns an empty stack """
    return ArrayStack([None], 1, 0)


def push(stack: ArrayStack, value: Any) -> None:
    """Place value on top of the stack, resizing if needed."""
    if stack.size == stack.capacity:
        stack.capacity *= 2
        stack.array = stack.array + [None] * (stack.capacity - stack.size)
    stack.array[stack.size] = value
    stack.size += 1

def pop(stack: ArrayStack) -> Any:
    """Takes a stack as an argument and removes (and returns)
    the element at the "top" of the stack. If the stack is empty, then
    this operation should raise an IndexError"""

    if stack.size <= 0: 
        raise IndexError(
            "No value to pop; please check your Array stack and try again"
        )
    stack.size -=1  #accounting for array-based indexing
    result = stack.array[stack.size]
    stack.array[stack.size] = None 
    return result 


def peek(stack: ArrayStack) -> Any:
    """takes a stack as arg and returns, w/o removing, the value on "top"
    of the stack. If the stack is empt, then this operation should raise an
    IndexError."""
    if stack.size <= 0: 
        raise IndexError(
            "Nothing to peek; Please check your ArrayStack and try again"
        )
    return stack.array[stack.size-1] 


def is_empty(stack: ArrayStack) -> bool:
    """This function takes a stack as an argument and returns whether stack is
    empty or not,Lowkey this is some bull, I can't even be good at
    programming without getting penalized."""
    return stack.size == 0 
        

def size(stack: ArrayStack) -> int:
    """Takes stack as arg and returns how many items in stack"""
    return stack.size 
