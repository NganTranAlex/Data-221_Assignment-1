# Safe Function Application
def compute_power_of_number_given_pairs(list_of_pairs):
    result = []
    for x, y in list_of_pairs:
        if y < 0: # skip of y is negative
            continue
        result.append(x ** y) # add to the list if the pair satisfy the condition
    return result

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
print(compute_power_of_number_given_pairs(pairs))



