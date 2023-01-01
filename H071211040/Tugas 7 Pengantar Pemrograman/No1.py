import re

s = input()

if len(s) == 45:
    syarat = r'^[a-zA-Z[02468]{40}[13579\s]{5}'

    pola = re.findall(syarat, s)

    if pola:
        print("True")
    else:
        print("False")

else:
    print('False')