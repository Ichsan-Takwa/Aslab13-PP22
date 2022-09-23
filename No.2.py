# SOAL NOMOR 2 PEKAN 2
# MAHENDRA KIRANA M.B. ( H071221058 )


GOLONGAN    = str  (input("Masukkan Golongan           : "))
DAYA        = float(input("Masukkan Daya (VA)          : "))
PEMAKAIAN   = float(input("Masukkan Pemakaian (Total)  : "))

if GOLONGAN == 'R1' : 
    if DAYA == 900 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1352}")
    elif DAYA >= 1300 and DAYA <= 2200 : 
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1444.70}")
    else :
        print("Data Tidak Valid")

elif GOLONGAN == "R2" :
    if DAYA >= 3500 and DAYA <= 5500 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1699.53}")
    else :
        print("Data Tidak Valid")

elif GOLONGAN == "R3" :
    if DAYA <= 6600 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1699.53}")
    else :
        print("Data Tidak Valid")

elif GOLONGAN == "B2" :
    if DAYA >= 6600 and DAYA <= 200000 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1444.70}")
    else :
        print("Data Tidak Valid")

elif GOLONGAN == "B3" :
    if DAYA >= 200000 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1114.74}")
    else :
        print("Data Tidak Valid")

elif GOLONGAN == "I3" :
    if DAYA > 200000 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1314.12}")
    else :
        print("Data Tidak Valid")

elif GOLONGAN == "P1" :
    if DAYA >= 6600 and DAYA <= 200000 :
        print(f"Jumlah Tagihan Anda : {PEMAKAIAN*1314.12}")

else :
    print("Data Tidak Valid")