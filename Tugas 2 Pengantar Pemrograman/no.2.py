golongan = str(input("Golongan = "))
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

if golongan == "R1":
    if daya == 900:
        print("Jumlah tagihan anda : ",1352*pemakaian)
    elif daya == 1300:
        print("Jumlah tagihan anda : ",144.70*pemakaian)
    elif daya == 2200:
        print("Jumlah tagihan anda : ",144.70*pemakaian)
    else:
        print("Data tidak valid")
        

elif golongan == "R2":
    if daya >= 3500 and daya <= 5500:
        print("Jumlah tagihan anda : ",1699.53*pemakaian)
    else:
        print("Data tidak valid")

elif golongan == "R3":
    if daya >= 6600:
         print("Jumlah tagihan anda : ",1699.53*pemakaian)
    else:
        print("Data tidak valid")

elif golongan == "B2":
    if daya >= 6600 and daya <= 200000:
        print("Jumlah tagihan anda : ",1444.70*pemakaian)
    else:
        print("Data tidak valid")

elif golongan == "B3":
    if daya > 200000:
        print("Jumlah tagihan anda : ",1114.74*pemakaian)
    else:
        print("Data tidak valid")

elif golongan == "I3":
    if daya >= 200000:
        print("Jumlah tagihan anda : ",1314.12*pemakaian)
    else:
        print("Data tidak valid")

elif golongan == "P1":
    if daya >= 6600 and daya <= 200000:
        print("Jumlah tagihan anda : ",1523.28*pemakaian)
    else:
        print("Data tidak valid")

else:
    print("Data tidak valid")
