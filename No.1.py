# JAWABAN NOMOR 1 SOAL PRAKTIKUM 

import math

h   =   int(input("Masukkan Tinggi Menara : "))
a   =   int(input("Masukkan Sudut elevasi pengamat Depan kapal : "))
b   =   int(input("Masukkan Sudut elevasi pengamat Belakang kapal : "))

rad =   (math.pi/180)*a 
x   =   math.tan(rad)

rad =   (math.pi/180)*b
y   =   math.tan(rad)

        Panjang_Kapal = round(h*x-h*y, 1)
        print("Maka Panjang Kapal : ", Panjang_Kapal, "m")