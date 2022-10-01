harga_barang = int(input("Harga Barang : "))
uang_yg_dibayarkan = int(input("Nominal Uang : "))

kembalian = uang_yg_dibayarkan-harga_barang
u1 = 0
u2 = 0
u3 = 0
u4 = 0
u5 = 0
u6 = 0
u7 = 0
if harga_barang < uang_yg_dibayarkan:
    while kembalian >= 100000:
        u1 += 1
        kembalian -= 100000

    while kembalian >= 50000:
        u2 += 1
        kembalian -= 50000

    while kembalian >= 20000:
        u3 += 1
        kembalian -= 20000

    while kembalian >= 10000:
        u4 += 1
        kembalian -= 10000

    while kembalian >= 5000:
        u5 += 1
        kembalian -= 5000

    while kembalian >= 2000:
        u6 += 1
        kembalian -= 2000

    while kembalian >= 1000:
        u7 += 1
        kembalian -= 1000
else:
    print("Inputan Tidak Valid")

print(u1, "uang Rp. 100.000" )
print(u2, "uang Rp. 50.000" )
print(u3, "uang Rp. 20.000" )
print(u4, "uang Rp. 10.000" )
print(u5, "uang Rp. 5.000" )
print(u7, "uang Rp. 2.000" )
print(u7, "uang Rp. 1.000" )