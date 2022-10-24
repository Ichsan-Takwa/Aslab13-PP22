x = int(input("x : "))
y = int(input("y : "))

if x < y:
    for i in range(1, y+1):
        print(i, end="\n" if i % x == 0 else " ")

else:
    print("error")
