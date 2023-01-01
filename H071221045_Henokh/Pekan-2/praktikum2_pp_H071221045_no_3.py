a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

besar = f"{a} adalah nilai terbesar" if a > b and a > c else f"{b} adalah nilai terbesar" if b > a and b > c else f"{c} adalah nilai terbesar"
print(besar)