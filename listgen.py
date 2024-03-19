import json
import random
import sys

try:
    list_size = int(sys.argv[1])
except IndexError:
    sys.exit('please provide list size as command line arg')
if list_size > 50000000:
    sys.exit("don't crash your computer... provide a smaller list")


with open('list.json', 'w') as f:  # 'w' clears the file every time
    rand_list = []
    for i in range(list_size):
        rand_list.append(random.randint(1, list_size))
    json.dump(rand_list, f)
