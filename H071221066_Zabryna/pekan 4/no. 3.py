#mayday

hari = int(input("Masukkan hari : "))
def myday(hari) :
    tahun = hari//360
    sisa_hari = hari%360
    bulan = sisa_hari//30
    hari1 = sisa_hari%30

    print("%d tahun" %(tahun))
    print("%d bulan" %(bulan))
    print("%d hari" %(hari1))

myday(hari)
