from typing import List

def load_names(path: str) -> List[str]:
    print(f"Loading names from path `{path}`...", end="", flush=True)
    with open(path) as txt_file:
        names = txt_file.read().splitlines()
        print("ok")
        return names

basic_names = load_names("names.txt")
sorted_names = load_names("sorted_names.txt")

from random import randint

def random_find(items, search_val):
    while True:
        rand_dex = randint(0, len(items)-1)
        rand_el = items[rand_dex]
        if rand_el == search_val:
            return rand_dex

def linear_find(items, search_val):
    for dex, val in enumerate(items):
        if val == search_val:
            return dex
    return None

def binary_iterative(elements, search_item):
    '''Return the index of the search_item or None if not found
       Only works if the data is sorted
    '''

    left, right = 0, len(elements) -1

    while left <= right:

        middle_dex = (left + right) // 2
        middle_el = elements[middle_dex]

        if middle_el == search_item:
            return middle_dex

        if middle_el < search_item:
            left = middle_dex + 1

        elif middle_el > search_item:
            right = middle_dex - 1

    return None

def binary_leftmost(elements, search_item):
    tentative = binary_iterative(elements, search_item)
    if tentative is None:
        return None

    while elements[tentative] == search_item and tentative >= 0:
        tentative -= 1
    return tentative + 1

def binary_recursive(elements, search_item, dex_mod=0):
    '''Return the index of the search_item or None if not found'''

    while elements:

        middle_dex = len(elements) // 2
        middle_el = elements[middle_dex]

        if middle_el == search_item:
            return middle_dex + dex_mod

        if middle_el < search_item:
            return binary_recursive(elements[middle_dex + 1:], search_item, dex_mod + middle_dex + 1)

        elif middle_el > search_item:
            return binary_recursive(elements[:middle_dex], search_item, dex_mod)

    return None