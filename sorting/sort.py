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

def insertion_sort(list_to_sort):
    """
    Sorts list of numbers in Theta(n^2) time.
    
    :param list_to_sort: list to sort
    :return: sorted list
    """
    for i in range(len(list_to_sort)):
        mem = list_to_sort[i]
        j = i-1
        while j>=0 and list_to_sort[j] > mem:
            list_to_sort[j+1] = list_to_sort[j]
            j -= 1
        list_to_sort[j+1] = mem
    return list_to_sort
    
def merge_sort(list_to_sort): 
    """
    Sorts list of numbers using divide-and-conquer paradigm.
    
    :param list_to_sort: list to sort
    :return: sorted list
    """
    n = len(list_to_sort)
    if n == 1:
        return list_to_sort
    left = merge_sort(list_to_sort[:mid])
    right = merge_sort(list_to_sort[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Subroutine used in merge_sort. 
    
    :param left: left array
    :param right: right array
    :return: merged array
    """
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1 
    if l < len(left):
        merged.extend(left[l:])
    if r < len(right):
        merged.extend(right[r:])
    return merged 
    
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
