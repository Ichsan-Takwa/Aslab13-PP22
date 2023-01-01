import re

S = input("")
regex = r"^[a-zA-Z24680]{40}[13579\s]{5}$"

x = re.findall(regex, S)

if x:
    print(True)
else:
    print(False)
