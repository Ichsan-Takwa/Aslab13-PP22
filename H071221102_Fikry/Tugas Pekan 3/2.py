x = float(input("derajat : "))
print ("program konversi waktu dari jumlah detik ke Jam/menit/detik")

t = x*24*3600/360+6*3600


jam = t //3600
sisa_detik= t -3600*jam 
menit=sisa_detik//60
detik=sisa_detik-(60*menit)

if jam > 24:
    jam = jam % 24
elif jam >= 00 and jam <= 4 :
    print ("Selamat Dini hari")
elif jam >= 4 and jam <= 10 :
    print ("Selamat Pagi")
elif jam >= 10 and jam <= 15 :
    print ("Selamat Siang")
elif jam >= 15 and jam <= 18 :
    print ("Selamat Sore")
else:
    print("Selamat Malam")
    
print ("%02d:%02d:%02d "%(jam,menit,detik))
