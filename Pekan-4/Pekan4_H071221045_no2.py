def getFPB(x, y):
    if x > y:
        kecil = y
    else:
        kecil = x
    for i in range(1, kecil+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i      
    return fpb

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"FPB dari {num1} dan {num2} = {getFPB(num1, num2)}")