rata = int(input("Masukkan rata-rata pemakaian listrik harian (Wh): "))

kwh = rata / 1000
tarif = (kwh * 1325) * 30
round(tarif, 2)

print("Jumlah tagihan listrik bulanan: Rp.", tarif)