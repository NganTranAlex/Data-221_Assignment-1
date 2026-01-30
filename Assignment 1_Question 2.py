# Nested Dictionary from Strings
def convert_list_of_strings_return_dictionary(list_of_strings):
    dictionary_of_strings = {} # an empty dictionary that will be storing the list of strings after it's converted
    for element in list_of_strings:
        length_of_string = len(element)
        if length_of_string % 2 == 0: # determine the parity of a string through the length of it
            parity_of_string = "even"
        else:
            parity_of_string = "odd"

        dictionary_of_strings[element] = {"length": length_of_string, "parity": parity_of_string}
    return dictionary_of_strings

print(convert_list_of_strings_return_dictionary(["data", "science"]))

