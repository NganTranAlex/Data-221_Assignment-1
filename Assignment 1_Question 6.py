# Distribution Analysis
def distribution_analysis(list_of_numbers):
    dictionary_of_numbers = {}
    # unique value: the number is only counted once no matter how many times it repeats
    total_of_numbers = len(list_of_numbers)

    unique_values = sorted(set(list_of_numbers)) # set executes any duplicates
    for current_value in unique_values:
        count_of_less_than_or_equal = 0
        for number in list_of_numbers:
            if number <= current_value:
                count_of_less_than_or_equal += 1

        percentage = (count_of_less_than_or_equal / total_of_numbers) * 100
        dictionary_of_numbers[current_value] = percentage

    return dictionary_of_numbers

print(distribution_analysis([3, 1, 2, 3, 4, 2]))
