def count_case_letters(input_str):
    upper_count = sum(1 for char in input_str if char.isupper())
    lower_count = sum(1 for char in input_str if char.islower())
    return upper_count, lower_count

# Example usage:
input_string = "Hello World"
upper, lower = count_case_letters(input_string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
