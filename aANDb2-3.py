import re
text="abb iam so sey and abbb dfdghjk 7890 abb abb abbb abbbb"
match=re.findall(r"ab{2,3}", text)
print(match)