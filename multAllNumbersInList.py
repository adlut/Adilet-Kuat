def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
numbers_list = [2, 3, 4, 5]
result = multiply_list(numbers_list)
print("Product of numbers:", result)
