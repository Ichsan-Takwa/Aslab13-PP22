harga = int(input("Masukkan Harga Barang: "))
uang = int(input("Masukkan Uang yang Dibayar: "))

sisa = uang - harga

seratus = sisa // 100000
print(f"{seratus} uang Rp. 100.000")
limapuluh = sisa % 100000 // 50000
print(f"{limapuluh} uang Rp. 50.000")
duapuluh = sisa % 100000 % 50000 // 20000
print(f"{duapuluh} uang Rp. 20.000")
sepuluh = sisa % 100000 % 50000 % 20000 // 10000
print(f"{sepuluh} uang Rp. 10.000")
lima = sisa % 100000 % 50000 % 20000 % 10000 // 5000
print(f"{lima} uang Rp. 5.000")
dua = sisa % 100000 % 50000 % 20000 % 10000 % 5000 // 2000
print(f"{dua} uang Rp. 2.000")
satu = sisa % 100000 % 50000 % 20000 % 10000 % 5000 % 2000 // 1000
print(f"{satu} uang Rp. 1.000")
koinlima = sisa % 100000 % 50000 % 20000 % 10000 % 5000 % 5000 % 1000 // 500
print(f"{koinlima} koin Rp. 500")
koindua = sisa % 100000 % 50000 % 20000 % 10000 % 5000 % 5000 % 1000 % 500 // 200
print(f"{koindua} koin Rp. 200")
koinsatu = sisa % 100000 % 50000 % 20000 % 10000 % 5000 % 5000 % 1000 % 500 % 200 // 100
print(f"{koinsatu} koin Rp. 100")