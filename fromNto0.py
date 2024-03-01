def generate_numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage:
n = int(input())
for num in generate_numbers_down_to_zero(n):
    print(num)
