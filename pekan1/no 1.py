#menghitung panjang kapal

import math

h = float(input("masukkan tinggi menara : "))
a = float(input("masukkan sudut elevasi pengamat terhadap ujung depan kapal : "))
b = float(input("masukkan sudut elevasi pengamat terhadp ujung belakang kapal : "))

rad = (math.pi/180)*a
x = math.tan(rad)

rad = (math.pi/180)*b
y = math.tan(rad)

panjang_kapal = round(h*x-h*y, 1)
print("Maka panjang kapal : ", panjang_kapal, "m")