import re
text="ab a abbb ghjk 19743 trgsw eas ac"
match=re.findall(r"\bab*\b", text)
print(match)
    