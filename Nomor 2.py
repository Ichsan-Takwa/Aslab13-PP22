# MAHENDRA KIRANA M.B
# H071221058

file1 = input()
file2 = input()

try :
    with open(f"{file1}.txt","r") as f :
        isi_file1 = f.readlines()
        terpanjang = isi_file1[0]

    for i in isi_file1 : # Mencari kalimat terpanjang pada isi file
        if len(i) > len(terpanjang) :
            terpanjang = i
            if '\n' not in terpanjang :
                terpanjang += (' ...')

    with open(f"{file2}.txt","w") as baru :
        for j in isi_file1 : # Menentukan banyak spasi untuk rata kanannya
         if '\n' in j :
            spasi = len(terpanjang) - len(j)
            baru.writer((' '*spasi)+j)
         else : # Untuk baris yang tidak memiliki enter atau baris terbawah
            beda = len(terpanjang) - len(j) - 1
            baru.writer((' '*beda)+j)
    print('Berhasil')
except :
    print('Gagal')
    
