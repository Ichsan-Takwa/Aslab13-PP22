#mencetak derajat kedalam bentuk satuan jam 

derajat = int(input("Masukkan derajat : "))
derajat_max = int(360)
waktu_max = int(86400)
waktu = (derajat/derajat_max)*waktu_max + 21600

jam = waktu//3600
sisa_detik = waktu%3600
menit = sisa_detik//60
detik = sisa_detik%60

jam%=24

if jam > 5 and jam <= 11 :
    print("Selamat Pagi")
elif jam > 11 and jam < 15 :
    print("Selamat Siang")
elif jam >= 15 and jam <= 18 :
    print("Selamat Sore")
elif jam > 18 and jam <= 24 :
    print("Selamat Malam")
elif jam >= 0 and jam <= 5 :
    print("Dini hari")
    
print("%02d:%02d:%02d" % (jam, menit, detik))