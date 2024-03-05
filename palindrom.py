def is_palindrome(input_str):
    return input_str == input_str[::-1]

# Example usage:
input_str = "madam"
result = is_palindrome(input_str)
print("Is palindrome:", result)
