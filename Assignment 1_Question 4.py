# Sorted Search with Conditions
from random import random

values = [random() for i in range(20)]
x = random()

values.sort() # sort the list

first_index = None
for i in range(len(values)):
    if values[i] >= x: # find indices where the list value is greater than or equal to x
        first_index = i
        break

print("Sorted list: ", values)
print("The value of x: ", x)

if first_index is not None: # find the first matching index (if exists)
    print("First matching index: ", first_index)