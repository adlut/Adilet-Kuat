def all_true_elements(input_tuple):
    return all(input_tuple)

bool_tuple = (True, True, 1, True)
result = all_true_elements(bool_tuple)
print("All elements are true:", result)
