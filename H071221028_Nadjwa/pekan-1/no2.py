#konvesi detik ke dalam format jam:menit:detik

detik = int(input('masukkan jumlah detik yang ingin di hitung'))
#menggunakan int karena mau memasukkan jumlah angka

jam= detik // 3600 
#mengunakan // supaya membulatkan angka agar tidak berkoma
sisa_detik= detik%3600 
# menggunakan _ untuk menyambungkan 2 variabel kata, dan menggunakan % untuk modulus 
menit = sisa_detik // 60
detik= sisa_detik % 60 

print(jam,':',menit,':',detik,'')
#menggunakan string : untuk menampilkan titik 2 pada output
