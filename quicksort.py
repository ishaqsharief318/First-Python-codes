import random

def quick_sort(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        left = quick_sort([i for i in list[1:] if i < pivot])
        right = quick_sort([i for i in list[1:] if i >= pivot])
        return left + [pivot] + right

some_list = random.sample(range(100),10)

print some_list

print quick_sort(some_list)

