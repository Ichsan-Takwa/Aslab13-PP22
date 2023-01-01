a = int(input("Masukkan Angka Pertama: "))
b = int(input("Masukkan Angka Kedua: "))
def getFPB(a,b):
    if a > b:
        lebih_kecil = b
    else:
        lebih_kecil = a
    for i in range (1,lebih_kecil+1):
        if(a % i == 0) and (b % i == 0):
            fpb = i
    return fpb

print("FPB",(a,b)," = ",getFPB(a,b))