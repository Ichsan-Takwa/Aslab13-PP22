harga = int(input("Masukkan Harga Barang: "))
uang = int(input("Masukkan Uang yang Dibayar: "))

sisa = uang - harga

seratus = 0
limapuluh = 0
duapuluh = 0
sepuluh = 0
lima = 0
dua = 0
satu = 0
klima = 0
kdua = 0
ksatu = 0

while sisa != 0:
    if sisa >= 100000:
        sisa = sisa - 100000
        seratus+=1
    elif sisa >= 50000:
        sisa = sisa - 50000
        limapuluh+=1
    elif sisa >= 20000:
        sisa = sisa - 20000
        duapuluh+=1
    elif sisa >= 10000:
        sisa = sisa - 10000
        sepuluh+=1
    elif sisa >= 5000:
        sisa = sisa - 5000
        lima+=1
    elif sisa >= 2000:
        sisa = sisa - 2000
        dua+=1
    elif sisa >= 1000:
        sisa = sisa - 1000
        satu+=1
    elif sisa >= 500:
        sisa = sisa - 500
        klima+=1
    elif sisa >= 200:
        sisa = sisa - 200
        kdua+=1
    else:
        sisa = sisa - 100
        ksatu+=1

print(f"{seratus} uang Rp. 100.000")
print(f"{limapuluh} uang Rp. 50.000")
print(f"{duapuluh} uang Rp. 20.000")
print(f"{sepuluh} uang Rp. 10.000")
print(f"{lima} uang Rp. 5.000")
print(f"{dua} uang Rp. 2.000")
print(f"{satu} uang Rp. 1.000")
print(f"{klima} koin Rp. 500")
print(f"{kdua} koin Rp. 200")
print(f"{ksatu} koin Rp. 100")
