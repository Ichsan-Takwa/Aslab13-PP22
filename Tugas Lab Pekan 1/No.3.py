# JAWABAN NO 3 PRAKTIKUM

    import math


r   = int   (input("Masukkan Jari-Jari Alas  : "))
t   = int   (input("Masukkan Tinggi          : "))   
phi = float (input("Masukkan Nilai phi       : "))

s   = math.sqrt((r*r) + (t*t))

        V   = 1/3*phi*r*r*t
        L   = phi*r*(s + r)

print("Maka Volume          : ",(round(V, 2)))
print("Maka Luas Permukaan  : ",(round(L, 2)))

