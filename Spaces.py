import re

pattern = re.compile(r'(?<=[a-z])([A-Z])')

# Example usage:
input_string = "InsertSpacesBetweenWords"
result = pattern.sub(r' \1', input_string)
print("Result:", result)
