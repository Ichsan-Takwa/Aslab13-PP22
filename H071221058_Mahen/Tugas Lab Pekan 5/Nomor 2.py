
print("==============================================================")
print("Selamat Datang! Untuk Memulai, Silahkan Input Data Anda")
print("==============================================================")

nama    = str(input("Input Nama :"))
umur    = int(input("Input Umur : "))
alamat  = str(input("Input Alamat : "))

profile = {"Nama"   : nama, 
           "Umur"   : umur,
           "Alamat" : alamat}

while True :
    print("==============================================================")#
    print(f'Selamat Datang {nama},Silahkan Pilih Opsi')
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("==============================================================")
    opsi = int(input("Input Opsi : "))
    print("==============================================================")

    if opsi == 1 :
        print("Data Anda Adalah")
        print("Nama :",profile['Nama'])
        print("Umur :",profile['Umur'])
        print("Alamat :",profile['Alamat'])
    elif opsi == 2 :
        nama = input("Silahkan Input Data Nama Baru :")
        profile['Nama'] = nama
        print("Data and sukses diperbaharui")
    elif opsi == 3 :
        umur = int(input("Silahkan Input Data Umur Baru :"))
        profile['Umur'] = umur
        print("Data anda sukses diperbaharui")
    elif opsi == 4 :
        alamat = input("Silahkan Input Data Alamat Baru :")
        profile['Alamat'] = alamat
        print("Data anda sukses diperbaharui")
    elif opsi == 5 :
        print(f'Selamat tinggal {nama}')
        break
    else :
        print("Opsi salah, Masukkan ulang opsi yang benar!")

