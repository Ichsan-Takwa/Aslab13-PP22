# mengecek S terdiri dari 45 karakter

import re

try:
    string_s = input()
    pattern = re.fullmatch("[02468a-zA-Z]{40}[13579\s]{5}", string_s)
    if pattern :
        print("true")
    else:
        print("false")
except:
    print("false")