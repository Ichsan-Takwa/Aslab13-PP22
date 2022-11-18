# MAHENDRA KIRANA M.B
# H071221058

file = input("Nama File : ")
jumlah = int(input("Jumlah Data : "))

nama = []
nim = []
angkatan = []

for i in range(jumlah) : #Perulangan untuk isi biodata sebanyak jumlah yang kita mau
    isi_nama = input('Masukkan Nama : ').replace(' ','_')
    if len(isi_nama) <= 20 :
        nama.append(isi_nama)
    else :
        print('Gagal')
        exit()
    isi_nim = input('Masukkan NIM : ')
    nim.append(isi_nim)
    isi_angkatan = input('Masukkan Angkatan : ')
    angkatan.append(isi_angkatan)

if len(isi_nama) <= 20 :
    with open(f"{file}.txt","w") as f :
        nama_terpanjang = nama[0]
        for panjang in nama : #Mencari nama yang terpanjang
            if len(panjang) > len(nama_terpanjang) :
                nama_terpanjang = panjang

        f.write('+-'+('-'*len(nama_terpanjang))+'-+') #Baris pertama atau paling atas dari tabel
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        f.write('\n| Nama' + (' '*(len(nama_terpanjang)-5))+'  |') #Baris kedua untuk kolom format nama, NIM, angkatan
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        f.write('\n+-'+(' '*len(nama_terpanjang))+'-+') #Baris ketiga batas antara format dan isi
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        for x in range(jumlah) : #Baris selanjutnya isi sesuai banyak data yang di input
            f.write('\n| ')
            f.write(nama[x])
            f.write(' '*(len(nama_terpanjang)-len(nama[x]))+' | ')
            f.write(nim[x])
            f.write(' '*(11-len(nim[x]))+' | ')
            f.write(angkatan[x])
            f.write((' '*(9-len(angkatan[x])))+'|')

        f.write('\n+-'+(' '*len(nama_terpanjang))+'-+') #Baris paling akhir sebagai penutup
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        print('Berhasil')

