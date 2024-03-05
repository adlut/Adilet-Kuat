import re

pattern = re.compile(r'[ ,.]')

input_string = "This is a test, for replacing spaces and dots."
result = pattern.sub(':', input_string)
print("Result:", result)
