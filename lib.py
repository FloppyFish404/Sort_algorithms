import time
import random

# TODO heap, counting, radix, bucket, shell, cocktail, comb
methods = {'selection', 'merge', 'tim', 'bubble', 'bogo',
           'insertion', 'quick'}


def print_time(method, time_taken):
    if time_taken > 60.0:
        time_taken = 60.0
        print('{} - execution time:   > {:.5f} seconds'
              .format(method.__name__[:3], time_taken))
    else:
        print('{} - execution time: {:>12.5f} seconds'
              .format(method.__name__[:3], time_taken))


def selection(lst):
    if len(lst) > 60000:
        return 999.0
    start_time = time.time()

    largest_num = len(lst) + 1  # largest possible num + 1
    sorted_list = []
    while len(lst) > 0:
        smallest = largest_num
        indx = None
        for i, num in enumerate(lst):
            if num < smallest:
                smallest = num
                indx = i
        sorted_list.append(smallest)
        lst.pop(indx)

    time_taken = time.time() - start_time
    return time_taken


def merge(lst):
    if len(lst) > 15000000:
        return 999.0
    start_time = time.time()
    merge_sort(lst)
    time_taken = time.time() - start_time
    return time_taken


# counter = [0]
def merge_sort(lst):

    # counter[0] += 1
    # print('count:', counter[0], lst)

    if len(lst) > 1:

        # split list
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        # print('\nlst', lst, 'left', left, 'right', right)
        merge(left)  # does nothing if len == 1
        merge(right)  # does nothing if len == 1

        i = 0
        j = 0
        k = 0

        # compare lists and sort
        while i < len(left) and j < len(right):
            # print('lst[k]', lst[k], 'left', left[i], 'right', right[j])
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                lst[k] = right[j]
                j += 1
            # print('lst[%d]' % k, '=', lst[k])
            k += 1

        while i < len(left):  # remainder of left list
            # print('lst[k]', lst[k], 'left', left[i], 'right', right[j-1])
            lst[k] = left[i]
            # print('lst[%d]' % k, '=', lst[k])
            i += 1
            k += 1

        while j < len(right):  # remainder of right list
            # print('lst[k]', lst[k], 'left', left[i-1], 'right', right[j])
            lst[k] = right[j]
            # print('lst[%d]' % k, '=', lst[k])
            j += 1
            k += 1
    # print('exiting recursive loop', lst)


def tim(lst):  # pythons default
    if len(lst) > 99999999999999:
        return 999.0
    start_time = time.time()
    sorted(lst)
    time_taken = time.time() - start_time
    return time_taken


def bubble(lst):
    if len(lst) > 50000:
        return 999.0

    start_time = time.time()

    done = False
    last = len(lst)
    while not done:
        switched = False
        for i in range(last-1):
            if lst[i] > lst[i+1]:
                smaller = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = smaller
                switched = True
        if not switched:
            done = True
        last -= 1  # optimisation: largest int always taken to the end / sorted

    time_taken = time.time() - start_time
    return time_taken


def bogo(lst):
    if len(lst) > 11:
        return 999.0
    start_time = time.time()

    ordered = False
    while not ordered:
        random.shuffle(lst)
        # check if ordered
        ordered = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                ordered = False

    time_taken = time.time() - start_time
    return time_taken


def insertion(lst):
    if len(lst) > 100000:
        return 999.0
    start_time = time.time()

    num = 1
    while num < len(lst):
        for i in range(0, num):
            if lst[i] > lst[num]:
                # print(lst)
                # print('lst[i] =', lst[i], 'lst[num] =', lst[num])
                # print('inserting', lst[num], 'at', i)
                lst.insert(i, lst[num])  # (before) pos = arg1, item = arg2
                # print(lst)
                # print('popping', lst[num+1], 'at', num+1)
                lst.pop(num + 1)
                break
        num += 1

    time_taken = time.time() - start_time
    return time_taken


def quick(lst):
    if len(lst) > 20000000:
        return 999.0
    start_time = time.time()

    quick_sort(lst, 0, len(lst))

    time_taken = time.time() - start_time
    return time_taken


def quick_sort(lst, start, end):
    # print('new call', start, end)

    if start < end - 1:  # min length 2
        split = partition(lst, start, end)
        quick_sort(lst, start, split)
        quick_sort(lst, split + 1, end)  # split+1 as pivot in exact right spot

        # print(lst)
    # else:
        # print('ignore')


def partition(lst, start, end):
    pivot = lst[end-1]
    j = start-1  # high pointer
    # print(lst[start:end], pivot)
    for i in range(start, end-1):
        # print('i =', i, '   j =', j)
        if lst[i] <= pivot:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
            # print('swapped pos', i, j)
    j += 1
    lst[end-1], lst[j] = lst[j], lst[end-1]  # swap pivot element
    # print('pivot swap', end-1, j)

    return j


def template(lst):
    if len(lst) > 100000:
        return 999.0
    start_time = time.time()

    pass  # method logic here

    time_taken = time.time() - start_time
    return time_taken

# TODO
"""
- write single sentence summary of what each algo does
- binary search
"""
