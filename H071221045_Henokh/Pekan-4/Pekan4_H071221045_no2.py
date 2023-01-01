def getFPB(x, y):
    kecil = y if x > y else x
    for i in range(kecil, 0, -1):
        if((x % i == 0) and (y % i == 0)):
            return i

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"FPB dari {num1} dan {num2} = {getFPB(num1, num2)}")
