list = [["Budi", "H001", "Laki-laki"], ["Siti", "H002", "Perempuan"]
]

i = 1

while True:
    print("="*30)
    print("             Menu")
    print("-"*30)
    print("0.] Exit\n1.] Tambah data Mahasiswa\n2.] Hapus data Mahasiswa\n3.] Edit data Mahasiswa\n4.] Tampilkan daftar Mahasiswa")
    print("="*30)
    pilih = input("> Pilih: ")
    print("="*30)
    if pilih == '1':
        i+=1
        nama = input("Nama: ")
        nim = input("NIM: ")
        kelamin = input("Jenis Kelamin: ")
        print("-"*30)
        list.append([])
        list[i].append(nama)
        list[i].append(nim)
        list[i].append(kelamin)
        print("-"*30)
        print("  Sukses Menambahkan Data")
        print('-'*30)
        print(list)
        print(len(list))
    elif pilih == '2':
        delete = int(input("Masukkan index yang ingin di delete (mulai dari 1): "))
        delete-=1
        list.pop(delete)
        print("-"*30)
        print("    Sukses Menghapus Data")
        print('-'*30)
    elif pilih == '3':
        edit = int(input("Masukkan index yang ingin di edit (mulai dari 1): "))
        edit-=1
        namabaru = input("Masukkan Nama yang baru: ")
        nimbaru = input("Masukkan NIM yang baru: ")
        kelaminbaru = input("Masukkan Jenis Kelamin yang baru: ")
        list[edit][0] = namabaru
        list[edit][1] = nimbaru
        list[edit][2] = kelaminbaru
        print('-'*30)
        print("     Sukses Mengedit Data")
        print('-'*30)
    elif pilih == '4':
        print("-"*30)
        for i in range(len(list)):
            print(f"Nama : {list[i][0]}")
            print(f"NIM : {list[i][1]}")
            print(f"Jenis Kelamin : {list[i][2]}")
            print("-"*30)
    elif pilih == '0':
        break
    else:
        print("Silahkan coba lagi")