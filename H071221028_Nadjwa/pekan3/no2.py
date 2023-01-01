derajat = float(input('Masukkan derajat:'))
waktu_max = int(86400)
derajat_max = int(360)
waktu = (derajat/derajat_max)*waktu_max

jam= (waktu // 3600)+6
sisa_detik= waktu %3600 
menit = sisa_detik // 60
detik= sisa_detik % 60 

if jam >= 5 and jam <= 10 :
    print ('Selamat Pagi')
elif jam > 10 and jam <= 15:
    print ('Selamat siang')
elif jam > 15 and jam <= 18 :
    print ('Selamat sore')
elif jam >18 and jam<= 24 :
    print ('Selamat malam:')
elif jam >24 and jam < 5 :
    print ('Selamat Tengah Malam')

print('%02d : %02d : %02d' % ((jam)%24, menit , detik))
