#menghitung luas dan volume kerucut
import math

t = float(input("Masukkan tinggi : "))
r = float(input("Masukkan jari jari : "))

s = math.sqrt((r*r)+(t*t))
phi = 3.14

Luas = round(phi*r*(s + r), 2)
Volume = round(1/3*phi*r*r*t, 2)

print("Luas kerucut : ", Luas)
print("Volume kerucut : ", Volume)
