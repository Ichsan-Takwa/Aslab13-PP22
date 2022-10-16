x = int(input("Masukkan Angka Faktorial: "))
def faktorial(x):
    if  x == 1:
        return x
    else:
        return x * faktorial(x-1)
    
print(faktorial(x))