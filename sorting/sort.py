import random

class NotIntegerError(ValueError): pass 
class NotNonNegativeError(ValueError): pass 

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
    Sorts list of numbers in O(n^2) time.
    
    :param list_to_sort: list to sort
    :return: sorted list
    """
    for i in range(len(list_to_sort)):
        mem = list_to_sort[i]
        j = i-1
        while j >= 0 and list_to_sort[j] > mem:
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
    
def counting_sort(list_to_sort):
    """
    Sorts list of non-negative numbers in pseudolinear time by counting the items.  
    
    :param list_to_sort: list to sort
    :return: sorted list
    """
    list_max = None
    for x in list_to_sort:
        if not isinstance(x,int):
            raise NotIntegerError("Input contains values other than integers.")
        if x < 0: 
            raise NotNonNegativeError("Intput contains values which are not non-negative.")
        if not list_max or list_max < x: 
            list_max = x 
    pos = [0] * (list_max + 1)
    for x in list_to_sort:
        pos[x] += 1 
    m = len(list_to_sort)
    for i in range(len(pos)-1, -1, -1):
        pos[i] = m - pos[i] 
        m = pos[i] 
    sorted_list = [None] * len(list_to_sort) 
    for x in list_to_sort:
        sorted_list[pos[x]] = x 
        pos[x] += 1 
    return sorted_list 
    
def binary_insertion_sort(list_to_sort):
    """
    Sorts list of numbers in O(n^2) time and O(n*log_2(n)) comparisons.
    
    :param list_to_sort: list to sort
    :return: sorted list
    """
    for i in range(len(list_to_sort)):
        mem = list_to_sort[i]
        k = recursive_binary_search(list_to_sort, mem, 0, i-1)
        j = i-1
        for _ in range(i-k):
            list_to_sort[j+1] = list_to_sort[j]
            j -= 1
        list_to_sort[j+1] = mem
    return list_to_sort 

def recursive_binary_search(alist, key, l=None, h=None):
    """
    Subroutine used in binary_insertion_sort. 
    
    :param alist: list on which to search 
    :param key: key to search  
    :param l: start index 
    :param h: end index 
    :return: position where to insert key 
    """
    if l == None: l = 0 
    if h == None: h = len(alist) - 1 
    if l <= h: 
        middle = l + (h-l) // 2 
        if key > alist[middle]:
            l = middle + 1 
        else: 
            h = middle - 1 
        return recursive_binary_search(alist, key, l, h)
    return l
   
def bubble_sort(list_to_sort):
    """
    Sorts a list by repeatedly stepping through the list, where each pair of 
    adjacent items is compared and swapped if the elements are in the wrong order. 
        
    :param list_to_sort: list to sort
    :return: sorted list
    """
    n = len(list_to_sort)
    for i in range(n):
        for j in range(n-1, i, -1):
            if list_to_sort[j] < list_to_sort[j-1]:
                list_to_sort[j], list_to_sort[j-1] = list_to_sort[j-1], list_to_sort[j]
    return list_to_sort 

def modified_bubble_sort(list_to_sort):
    """
    Sorts a list by repeatedly stepping through the list, where each pair of 
    adjacent items is compared and swapped if the elements are in the wrong order. 
    If no exchanges occurred during the last pass, the  while loop terminates. 
        
    :param list_to_sort: list to sort
    :return: sorted list
    """
    n = len(list_to_sort)
    exchanges = True 
    i = 0
    while i < n and exchanges:
        exchanges = False
        for j in range(n-1, i, -1):
            if list_to_sort[j] < list_to_sort[j-1]:
                exchanges = True 
                list_to_sort[j], list_to_sort[j-1] = list_to_sort[j-1], list_to_sort[j]
        i += 1 
    return list_to_sort 

def quick_sort(list_to_sort, p=None, r=None):
    """
    Sorts a list by repeatedly dividing it into two partitions according to a pivot. 
        
    :param list_to_sort: list to sort
    :param p: start index 
    :param r: end index 
    """
    if p == None: p = 0
    if r == None: r = len(list_to_sort) - 1
    if p < r:
        q = partition(list_to_sort, p, r)
        quick_sort(list_to_sort, p, q-1)
        quick_sort(list_to_sort, q+1, r)
        
def partition(alist, p, r):
    """
    Subroutine used in quick_sort. 
    
    :param alist: list to be partitioned
    :param p: start index
    :param r: end index
    :return: index of pivot
    """
    x = alist[r]
    i = p - 1
    for j in range(p, r):
        if alist[j] <= x:
            i = i + 1 
            alist[j], alist[i] = alist[i], alist[j] 
    alist[r], alist[i+1] = alist[i+1], alist[r]
    return i + 1
            
def randomised_quick_sort(list_to_sort, p=None, r=None): 
    """
    Sorts a list by repeatedly dividing it into two partitions according to a pivot, 
    where the pivot is chosen at random by randomised_partition. 
        
    :param list_to_sort: list to sort
    """
    if p == None: p = 0
    if r == None: r = len(list_to_sort) - 1 
    if p < r: 
        q = randomised_partition(list_to_sort, p, r)
        randomised_quick_sort(list_to_sort, p, q-1)
        randomised_quick_sort(list_to_sort, q+1, r)
        
def randomised_partition(alist, p, r):
    """
    Subroutine used in qrandomised_quick_sort. 
    
    :param alist: list to be partitioned
    :param p: start index
    :param r: end index
    :return: index of pivot 
    """
    i = random.randrange(p, r+1)
    alist[r], alist[i] = alist[i], alist[r]
    return partition(alist, p, r)

def shell_sort(alist):
    """
    Sorts a list by first sorting far apart elements, 
    then making the gap progressively smaller. 
        
    :param list_to_sort: list to sort
    """
    gap = len(alist) // 2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(alist, start, gap)
        print("After increments of size", gap, "The list is", alist)
        gap = gap // 2

def gap_insertion_sort(alist, start, gap):
    """
    Subroutine used in shell_sort. 
    
    :param alist: list to be sorted
    :param start: start index 
    :param gap: gap between elements
    """
    n = len(alist)
    for i in range(start+gap, n, gap):
        mem = alist[i]
        j = i - gap
        while j >= 0 and alist[j] > mem:
            alist[j+gap] = alist[j]
            j = j - gap
        alist[j+gap] = mem

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
