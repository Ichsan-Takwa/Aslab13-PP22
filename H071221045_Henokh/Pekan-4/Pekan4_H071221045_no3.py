def myDay(tgl):
    tahun = tgl//360
    bulan = tgl%360//30
    hari = tgl%360%30
    print(f"{tahun} tahun")
    print(f"{bulan} bulan")
    print(f"{hari} hari")
hari = int(input("Masukkan total hari: "))
myDay(hari)
