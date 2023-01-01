a = int(input('harga barang : Rp. '))
b = int(input('uang pembayaran : Rp. '))
c = b-a 
d = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

print("kembaliannya sebesar Rp.", c, "dengan rincian kembalian :")

for i in d :
    banyak_pecahan = c//i
    c = c - (i*banyak_pecahan)
    print(banyak_pecahan, "uang Rp.", i) 