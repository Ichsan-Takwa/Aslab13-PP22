# 3600 detik = 15 derajat
# 240 deik = 1 derajat
s = float(input("Masukkan Derajat : "))
detik = s*240
h= 6
m = 0
if s >= 0 and s <=360:
    while detik >= 3600:
        h += 1
        detik-=3600
        
    while detik >= 60:
        m += 1
        detik-=60

    if h >= 24:
        h -= 24

    if h <= 6 and h < 12:
        print("Selamat Pagi\n",h,":",m,":",int(detik))
    elif h >= 12 and h < 15:
        print("Selamat Siang\n",h,":",m,":",int(detik))
    elif h >= 15 and h < 18:
        print("Selamat Sore\n",h,":",m,":",int(detik))
    elif h >= 18:
        print("Selamat Malam\n",h,":",m,":",int(detik))
else:
    print("Inputan Tidak Valid")