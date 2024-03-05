import re

pattern = re.compile(r'[a-z]+_[a-z]+')

# Example usage:
test_string = "example_string AShjgfk_rjfS"
matches = pattern.findall(test_string)
print("Matches:", matches)
