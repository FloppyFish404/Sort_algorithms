import time

methods = {'selection', 'merge'}
# methods = ['selection', 'merge' 'insertion', 'merge', 
#           'quick', 'heap', 'bubble', 'comb', 'cocktail']


def selection(list1):
    start_time = time.time()
    largest_num = len(list1) + 1  # largest possible num + 1
    sorted_list = []
    while len(list1) > 0:
        smallest = largest_num
        indx = None
        for i, num in enumerate(list1):
            if num < smallest:
                smallest = num
                indx = i
        sorted_list.append(smallest)
        list1.pop(indx)
    time_taken = time.time() - start_time
    list1 = sorted_list
    return time_taken


def merge(lst):  # noqa
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
