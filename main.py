import lib
import json
import sys

with open('list.json') as f:
    list1 = json.load(f)

time_taken = 0.0
complete = False

while not complete:
    method = input('What sort method would you like to use?\n')

    if method == 'all':
        for method in lib.methods:
            method = getattr(lib, method)
            time_taken = method(list1)
            print('{} - execution time: {:>10.3f} seconds'
                  .format(method.__name__[:3], time_taken))
            with open('list.json') as f:  # reset list
                list1 = json.load(f)
        complete = True

    elif method in lib.methods:
        method = getattr(lib, method)
        time_taken = method(list1)
        print('{} - execution time: {:>10.3f} seconds'
              .format(method.__name__[:3], time_taken))
        complete = True

    else:
        print("\nSelect a valid method, these include: {}\n"
              .format(', '.join(lib.methods)))
