import json
import time

start_time = time.time()

with open('list.json') as f:
    list1 = json.load(f)

list_size = len(list1) + 1  # largest possible num + 1

sorted_list = []
while len(list1) > 0:
    smallest = list_size
    indx = None
    for i, num in enumerate(list1):
        if num < smallest:
            smallest = num
            indx = i
    sorted_list.append(smallest)
    list1.pop(indx)

end_time = "execution time: %s seconds" % (time.time() - start_time)
print(end_time)
