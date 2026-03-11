from __future__ import annotations

from typing import Any


def selection_sort(lst: list[Any]) -> int:
    """Sorts the given list with selection sort.

    Returns the number of comparisons made.
    """ 
    comparison_count = 0 

    if len(lst) <= 1: 
        return comparison_count

    for idx in range(0, len(lst)-1):
        small_idx = idx

        for j in range(idx + 1, len(lst)): 

            if lst[j] < lst[small_idx]:
                small_idx = j 

            comparison_count += 1 

        lst[idx], lst[small_idx] = lst[small_idx], lst[idx]

    return comparison_count

#come back to this
def insertion_sort(lst: list[Any]) -> int:
    """Sorts the given list with insertion sort.

    Returns the number of comparisons made.
    """
    comparison_count = 0

    if len(lst) <= 1: 
        return comparison_count 

    for idx in range(1, len(lst)):
        sort = lst[idx]
        j = idx - 1
        
        while j >= 0:
            comparison_count += 1
            if lst[j] > sort: 
                lst[j+1] = lst[j]
                j -=1
            else:
                break

        lst[j+1] = sort 

    return comparison_count


# NOTE: you shouldn't need to change any of the merge sort code.
def merge_sort(lst: list[Any]) -> int:
    """Sorts the given list with merge sort.

    Returns the number of comparisons made.
    """
    # Make a copy of the given list and use it as the source for the
    # sort.  The sorted results will then be placed back into the given
    # list.
    return merge_sort_partial(lst.copy(), lst, 0, len(lst))


def merge_sort_partial(
    source_list: list[Any],
    target_list: list[Any],
    start: int,
    end: int,
) -> int:
    """Sorts the elements in source_list between the start and end.

    Places the sorted result in target_list.

    Returns the number of comparisons made.
    """
    comparisons = 0

    # If there are at least 2 things to sort
    if end - start > 1:
        mid = (start + end) // 2

        # Recursively sort both halves.  We sort from the target_list
        # into the source_list here so that in the merge step, we merge
        # from the source_list back into the target list.
        comparisons += merge_sort_partial(target_list, source_list, start, mid)
        comparisons += merge_sort_partial(target_list, source_list, mid, end)

        # Merge the sorted source_list[start:mid] and
        # source_list[mid:end] into the target_list[start:end].
        comparisons += merge(source_list, target_list, start, mid, end)

    return comparisons


def merge(
    source_list: list[Any],
    target_list: list[Any],
    start: int,
    mid: int,
    end: int,
) -> int:
    """Merge the sorted source_list[start:mid] and source_list[mid:end].

    Places the result into target_list[start:end] in sorted order.

    Returns the number of comparisons made.
    """
    left = start
    right = mid
    target_index = start
    comparisons = 0

    # While both sides still have more data
    while left < mid and right < end:
        # Compare to see which is the smaller value, and put that next
        # into the target_list.
        comparisons += 1
        if source_list[left] < source_list[right]:
            target_list[target_index] = source_list[left]
            left += 1
        else:
            target_list[target_index] = source_list[right]
            right += 1
        target_index += 1

    # Transfer the rest of the items in the left to sorted list.
    while left < mid:
        target_list[target_index] = source_list[left]
        target_index += 1
        left += 1

    # Transfer the rest of the items in the right to sorted list.
    while right < end:
        target_list[target_index] = source_list[right]
        target_index += 1
        right += 1

    return comparisons
