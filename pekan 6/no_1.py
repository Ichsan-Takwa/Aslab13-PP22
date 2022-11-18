# menyalin file dengan extensi .txt

nama_file = input("Masukkan nama file : ")
file_copy = input("Masukkan nama file copy : ")
try:
    with open (nama_file+'.txt', 'r') as file :
        print(file.read())
        nama_file = file.read()
        file_copy = file.read()

    with open (file_copy+'.txt', 'w') as file :
        file.write(file_copy)

    print ('Berhasil')

except :
    print ('Gagal')