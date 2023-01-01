print ("program konversi waktu dari jumlah detik ke Jam/menit/detik")
print ("==========")
jumlah_detik = int(input("masukkan jumlah detik : "))

jam = jumlah_detik//3600
sisa_detik=jumlah_detik-3600*jam 
menit=sisa_detik//60
detik=sisa_detik-(60*menit)

print ("%02d:%02d:%02d "%(jam,menit,detik))
