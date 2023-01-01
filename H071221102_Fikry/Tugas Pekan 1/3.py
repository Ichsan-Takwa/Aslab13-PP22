#Nama seller, gaji pokok, dan total penjualan dalam bulan itu.

a = str(input("masukkan nama pertama seller : "))
b = float(input("masukkan gaji pokok : "))
c = float(input("masukkan total penjualan seller : "))
#saya menggunakan float untuk mengubah menjadi bilangan desimal
total = float(b + c *15/100)
#masukkan nilai b+c kemudian sesuai soal menerima 15% saya kalikan 15/100
#ubah persen menjadi 15/100
print ("total = $ " , round (total,2))
#untuk menghasilkan dollar, saya masukkan parameternya dengan total = $
#saya menggunakan round untuk membatasi angka dibelakang koma, dengan sesuai konteks soal 2 angka bilangan desimal
