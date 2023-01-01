# Nomor 2
# Mahendra Kirana M.B (H071221058)

x = int(input('Masukkan Nilai : '))
y = int(input('Masukkan NIlai : '))
def hitung_FPB(x,y) :
    if x > y :
        lebih_kecil = y
    else :
        lebih_kecil = x
    for i in range(1, lebih_kecil+1) :
        if((x % i == 0) and (y % i == 0)) :
            fpb = i
        return fpb
print("FPB dari (",x,",",y,") =", hitung_FPB(x,y))
