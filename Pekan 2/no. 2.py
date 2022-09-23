#informasi daya listrik dan total tagihan listrik 

golongan = str(input("golongan : "))
daya = int(input("daya (dalam VA) : "))
pemakaian = int(input("pemakaian listrik : "))

if golongan == 'R1' :
    if daya == 900 :
        print(f"jumlah tagihan : {1352*pemakaian}")
    elif daya >= 1350 and daya <= 2200 :
        print(f"jumlah tagihan : {1444.70*pemakaian}")
    else :
        print("Data tidak valid")
elif golongan == 'R2' :
    if daya >= 3500 and daya <= 5500 :
        print(f"jumlah tagihan : {1699.53*pemakaian}")
    else : 
        print("Data tidak valid")
elif golongan == 'R3' :
    if daya >= 6600 : 
        print(f"jumlah tagihan : {1699.53*pemakaian}")
    else : 
        print("Data tidak valid")
elif golongan == 'B2' :
    if daya >= 6600 and daya <= 200000 :
        print(f"jumlah tagihan : {1444.70*pemakaian}")
    else : 
        print("Data tidak valid")
elif golongan == 'B3' :
    if daya >= 200000 :
        print(f"jumlah tagihan : {1114.74*pemakaian}")
    else : 
        print("Data tidak valid")
elif golongan == 'I3' :
    if daya > 200000 :
        print(f"jumlah tagihan : {1314.12*pemakaian}")
    else : 
        print("Data tidak valid")
else : 
        print("Data tidak valid")