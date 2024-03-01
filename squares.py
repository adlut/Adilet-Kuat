def generate_squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Input values for a and b
a = int(input("Enter the starting value (a): "))
b = int(input("Enter the ending value (b): "))

# Test the generator with a for loop
for square in generate_squares(a, b):
    print(square)
