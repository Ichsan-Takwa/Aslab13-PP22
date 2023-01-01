def myDay():
    x = int(input("Masukkan usia dalam hari : "))
    if x >= 360:
        tahun = x // 360
        sisa = x % 360
        print(f"{tahun} tahun")

    if sisa >= 30:
        bulan = sisa // 30
        sisa_hari = sisa % 30
        print (f"{bulan} bulan")

    if sisa_hari >= 0:
        hari = sisa_hari
        print(f"{hari} hari")

myDay()
