# NOMOR 3 PRAKTIKUM PEKAN 3
# MAHENDRA KIRANA M.B(H071221058)

a = int(input('Harga Barang : Rp. '))
b = int(input('Uang Pembayaran : Rp. '))
c = b-a
d = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

print("Kembalian Sebesar Rp.", c, "Dengan Rincian Kembalian : ")

for i in d :
    Banyak_Pecahan = c//i
    c = c - (i*Banyak_Pecahan)
    print(Banyak_Pecahan, "Uang Rp.", i)