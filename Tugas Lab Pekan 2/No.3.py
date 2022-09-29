# NOMOR 3 PEKAN 2 PRAKTIKUM
# MAHENDRA KIRANA M.B. ( H071221058 )

angka = list(map(int, input("Masukkan Angka : ").split()))

for i in range(len(angka)) :
    angka[i] = int(angka[i])

try :
    angka_genap = sum(1 for i in angka if i%2 ==0)
    angka_ganjil = sum(1 for i in angka if i%2 != 0)
    angka_positif = sum(1 for i in angka if i > 0)
    angka_negatif = sum(1 for i in angka if i < 0)

    print(f"{angka_genap} Angka Genap")
    print(f"{angka_ganjil} Angka Ganjil")
    print(f"{angka_positif} Angka Positif")
    print(f"{angka_negatif} Angka Negatif")

except :
    print("Data Tidak Valid")




