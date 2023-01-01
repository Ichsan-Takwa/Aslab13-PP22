from ast import match_case

gol = input("Golongan = ")
daya = int(input("Daya = "))
pakai = int(input("Pemakaian = "))

gol1 = gol.upper()

match gol1:
    case "R1":
        if daya == 900:
            harga = pakai * 1352
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        elif daya == 1300:
            harga = pakai * 1444.70
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        elif daya == 2200:
            harga = pakai * 1444.70
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case "R2":
        if daya >= 3500 and daya <= 5500:
            harga = pakai * 1699.53
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case "R3":
        if daya >= 6600:
            harga = pakai * 1699.53
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case "B2":
        if daya >= 6600 and daya <= 200000:
            harga = pakai * 1444.70
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case "B3":
        if daya > 200000:
            harga = pakai * 1114.74
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case "I3":
        if daya >= 200000:
            harga = pakai * 1314.12
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case "P1":
        if daya >= 6600 and daya <= 200000:
            harga = pakai * 1523.28
            round(harga, 2)
            print(f"Jumlah tagihan anda: Rp.{harga:,}")
        else:
            print("data tidak valid")
    case _:
        print("data tidak valid")