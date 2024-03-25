import re

pattern=re.compile(r"[0-9]")

test="+7989526262626"
matches=pattern.findall(test)
print(matches)