def myDay(tgl):
    if(tgl >= 365):
        tahun = tgl//365
        myDay(tgl%365)
        print(f"{tahun} tahun")
    elif(tgl >= 30 and tgl < 365):
        bulan = tgl//30
        myDay(tgl%30)
        print(f"{bulan} bulan")
    else:
        print(f"{tgl} hari")
    return tgl
hari = int(input("Masukkan total hari: "))
myDay(hari)
