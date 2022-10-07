# Nomor 3
# Mahendra Kirana M.B (H071221058)

a = int(input('Masukkan Hari : '))
def myday (a) :
    Tahun   = a//365
    sisa    = a%365
    Bulan   = sisa//30
    Hari    = sisa%30

    print('%d Tahun' % (Tahun))
    print('%d Bulan' % (Bulan))
    print('%d Hari' % (Hari))

myday(a)
