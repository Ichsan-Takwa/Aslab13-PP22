import math

derajat = float(input("Masukkan derajat matahari (0 - 360 derajat): "))

hitung = float(derajat/15)

jumlah = float((hitung * (3600)) + 21600)

jam = int(jumlah / 3600)
menit = int((jumlah % 3600) / 60)
detik = int((jumlah % 3600) % 60)

if jam > 24:
    jam1 = jam - 24
    if jam1 >= 6 and jam1 < 12:
        print("Selamat Pagi")
    elif jam1 >= 12 and jam1 < 16:
        print("Selamat Siang")
    elif jam1 >= 16 and jam1 < 19:
        print("Selamat Sore")
    else:
        print("Selamat Malam")
    print(f"{jam1:02d}:{menit:02d}:{detik:02d}")
else:
    if jam >= 6 and jam < 12:
        print("Selamat Pagi")
    elif jam >= 12 and jam < 16:
        print("Selamat Siang")
    elif jam >= 16 and jam < 19:
        print("Selamat Sore")
    else:
        print("Selamat Malam")
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")
