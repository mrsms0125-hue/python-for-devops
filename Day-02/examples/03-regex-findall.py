import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")








import re

text="AND1USER 1, USER 2 AND USER 3 HAVE LOG ON ANDAND2"

pattern=r"AND\d"
match1=re.match(pattern,text)
if match1:
    print(match1.group())
else:
    print("no match1")

match2=re.search(pattern,text)
if match2:
    print(match2.group())
else:
    print("no match2")

match3=re.findall(pattern,text)
print(match3[1])

