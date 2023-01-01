# menyalin file dan hasil salinannya rata kanan

nama_file = input("Maukkan nama file : ")    
file_copy = input("Masukkan nama file copy : ")

try:
    with open (nama_file+'.txt', 'r') as file :
        nama_file = file.readlines()
        print(nama_file)

        nama_file[-1] = nama_file[-1]+'\n'
        x = 0
        for i in nama_file:
            if len(i) > x:
                x = len(i)

    with open (file_copy+'.txt', 'w') as file :
        for i in nama_file :
            file.write(i.rjust(x))

    print ('Berhasil')

except :
    print ('Gagal')