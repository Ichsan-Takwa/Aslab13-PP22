#Program untung menghitung kembalian dari waktu transaksi

x = int(input("Harga barang : "))
y = int(input("Nilai uang yang dibayarkan  : "))
sisa = y - x

uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for i in uang_pecahan:
    if y >= x:
        banyak_pecahan = int(sisa/i)
        sisa = sisa - (i*banyak_pecahan)
        print("{} uang Rp. {}".format(banyak_pecahan,i))

    else:
        print("error")
        break
