import random


def shuffle_sort(list_to_sort):
    """
    Sorts list of numbers in stupidly inefficient way.

    :param list_to_sort: list to sort
    :return: sorted list
    """
    while not is_sorted(list_to_sort):
        random.shuffle(list_to_sort)
    return list_to_sort


def is_sorted(sorting_list):
    """Checks if list is sorted"""
    if len(sorting_list) == 1:
        return True
    previous = sorting_list[0]
    for number in sorting_list[1:]:
        if number < previous:
            return False
        previous = number
    return True
