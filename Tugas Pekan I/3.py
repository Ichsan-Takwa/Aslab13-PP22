#Nama seller, gaji pokok, dan total penjualan dalam bulan itu.

a = str(input("masukkan nama pertama seller : "))
b = float(input("masukkan gaji pokok : "))
c = float(input("masukkan total penjualan seller : "))

total = float(b + c *15/100)

print ("total = $ " , round (total,2))
