# NOTE: Change this file however you want.  I won't be grading it at
# all.  It's only used to generate the data for filling in the table.
import random
import time

from collections.abc import Callable
from typing import Any

from sorts import insertion_sort, merge_sort, selection_sort


def time_sort(
    sort_function: Callable[[list[Any]], int],
    size: int,
) -> tuple[float, int]:
    """Time the sort function on a random list of the given size.

    Returns the time and the number of camparisons as a tuple.
    """
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated each time.  This makes for a fair
    # comparison between sort functions, they'll be sorting the same
    # lists.  You're welcome to change the seed, but for a fair
    # comparison you'll want the same seed for each sort algorithm.
    random.seed(1234)
    my_list = random.choices(range(1000000), k=size)

    start_time = time.time()
    comparisons = sort_function(my_list)
    end_time = time.time()

    return end_time - start_time, comparisons


def main():
    # This is an example of how to use the above function.  I would
    # suggest making some loops here to collect all the data at once.
    while True:
        while True: 
            try:  
                size_input =input('enter size of list or e for exit: ')
                
                if isinstance(size_input, str):
                    size_input.lower()

                if size_input == 'e':
                    exit

                size = int(size_input)   
                break
            except ValueError: 
                print('Please enter int')
                print()

        while True: 
            sort_type = input(
                's -> selection, m -> merge,' \
                ' i -> insertion, e -> exit script:  '
                ).lower()
            
            if (
                sort_type == 's' or sort_type == 'm' or sort_type == 'i' or 
                sort_type == 'e'
            ):
                break
            else:    
                print('not valid input!')
                print()
            
        if sort_type == 'e':
            exit 

        elif sort_type == 'm':
            duration, comps = time_sort(merge_sort, size)
            sort_function = "Merge"

        elif sort_type == 's':
            duration, comps = time_sort(selection_sort, size)
            sort_function = "Selection"


        elif sort_type == 'i':
            duration, comps = time_sort(insertion_sort, size)
            sort_function = "Insertion"

        try: 

            print(
                f"{sort_function} sort ({size} elements):",
                f"{duration:.3f} s,",
                f"{comps}  comparisons",
            )
        except NameError: 
            print('variable not defined.')

if __name__ == "__main__":
    main()
