import re

pattern = re.compile(r'[A-Z][a-z]+')

# Example usage:
test_string = "CamelCaseExample we WDhm"
matches = pattern.findall(test_string)
print("Matches:", matches)
