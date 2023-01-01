import math 
h = float(input("masukkan ketinggian menara (dalam satuan vektor): "))
a = float(input("masukkan derajat sudut elevasi pengamat terhadap ujung belakang kapal: "))
b = float(input("masukkan derajat sudut elevasi pengamat terhadap ujung depan kapal: "))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan

print("panjang kapalnya adalah", panjang, "m")
