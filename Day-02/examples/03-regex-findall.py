import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")








import re

text="USER 1, USER 2 AND USER3 HAVE LOG ON ANDAND2"

pattern=r"USER\s\d"
match1=re.match(pattern,text)
if match1:
    print(match1.group())
    print("📍 Match starts at index:", match1.start())
    print("📍 Match ends at index:", match1.end())

else:
    print("no match1")

match2=re.search(pattern,text)
if match2:
    print(match2.group())
    print("📍 Match starts at index:", match2.start())
    print("📍 Match ends at index:", match2.end())
else:
    print("no match2")

match3=re.findall(pattern,text)
print(match3[1])
print(match3[0])


replaced_text=re.sub("USER3","USER 3",text)
print(replaced_text)

split_text=re.split(',',text)
print(split_text)
print(split_text[1])

###################################################
import re
log="Failed password for invalid user root from 203.0.113 port 22"

ip=re.search("\d{1,3}.\d.\d{1,3}.\d*",log)

print(ip.group())


#########################################

import re

email = "adm-in@@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

pattern1=r"^[\w\.\-]+@+[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email:", email)
else:
    print("Invalid email format")

if re.match(pattern1, email):
    print("In-Valid email: 2@", email)
else:
    print("valid email format")


