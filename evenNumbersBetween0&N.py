def generate_even_numbers(N):
    for i in range(0, N + 1, 2):
        yield i

# Example usage:
N = int(input("Enter a number (N): "))
even_numbers = generate_even_numbers(N)
print(','.join(map(str, even_numbers)))
