#FPB 2 inputan angka 

def getFPB(a, b):
    if (b==0):
        return a
    else :
        return getFPB(b, a%b)

a = int(input("Masukkan a : "))
b = int(input("Masukkan b : "))
print("FPB dari", a, "dan", b, "=", getFPB(a, b))