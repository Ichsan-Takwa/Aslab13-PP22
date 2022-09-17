import math
h = float(input("Masukkan Ketinggian Menara (dalam satuan meter): ")) 
a = float(input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal: "))
b = float(input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal: "))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
pjg = belakang-depan

print("Panjang Kapalnya adalah", pjg, "m")