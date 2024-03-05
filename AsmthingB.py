import re

pattern = re.compile(r'a.*b$')

test_string = "aanyb"
if pattern.fullmatch(test_string):
    print("Match found!")
else:
    print("No match.")

