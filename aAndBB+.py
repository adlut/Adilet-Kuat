import re

pattern = re.compile(r'abb+')

def match_string(input_string):
    return bool(pattern.match(input_string))
print(match_string("abbbb"))
print(match_string("abb"))
print(match_string("ab"))