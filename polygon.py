import math

while True:
    try:
        num_sides = int(input("Input number of sides (integer): "))
        break 
    except ValueError:
        print("Please enter a valid integer for the number of sides.")

while True:
    try:
        side_length = float(input("Input the length of a side: "))
        break 
    except ValueError:
        print("Please enter a valid number for the length of a side.")
area = int((num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides)))
print("The area of the polygon is:", area)
