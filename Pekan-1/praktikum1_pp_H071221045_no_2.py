jumlah = int(input("Masukkan Jumlah Detik: "))

jam = int(jumlah / 3600)
menit = int((jumlah % 3600) / 60)
detik = (jumlah % 3600) % 60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")
