#merubah detik ke format jam:menit:detik

detik = int(input("Masukkan detik : "))

jam = detik//3600
sisa_detik = detik%3600
menit = sisa_detik//60
detik = sisa_detik%60

print(jam, ":", menit, ":", detik)
