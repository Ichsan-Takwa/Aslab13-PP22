import math

nama = str(input("Nama Seller : "))
gajiPokok = float(input("Gaji Pokok : "))
totalPenjualan = float(input("Total Penjualan : "))

print (round(gajiPokok + (totalPenjualan*(15/100)),2)) 