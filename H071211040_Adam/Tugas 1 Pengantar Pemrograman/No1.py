import math

h = int(input("Masukkan Tinggi Mercusuar: "))
sudutA = int(input("Masukkan Besar Sudut A : "))
sudutB = int(input("Masukkan  Besar Sudut B : "))

x = h * math.tan(math.radians((sudutA)))
y = h * math.tan(math.radians((sudutB)))

print("Panjang Kapal Adalah ",round(x-y,1)," m")