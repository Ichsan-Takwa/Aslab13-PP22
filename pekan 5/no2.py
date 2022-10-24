print("Selamat datang untuk memulai silahkan input data Anda")
nama = input("Input nama : ")
umur = int(input("Input umur : "))
alamat = input("Input alamat : ")

data = {"nama" : nama, "umur" : umur, "alamat" : alamat}

while True :
    print("="*100)
    print(f"Halo {data['nama']} silahkan pilih opsi")
    print("="*100)
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
    print("="*100)

    opsi = int(input("Input opsi : "))

    print("="*100)

    if opsi == 1 :
        print("Data anda adalah : ")
        print(f"Nama : {data['nama']}")
        print(f"Umur : {data['umur']}")
        print(f"Alamat : {data['alamat']}")
    elif opsi == 2 :
        ubah_nama = input("Silahkan input nama baru : ")
        data['nama'] = ubah_nama
        print("Data anda sukses diperbarui")
    elif opsi == 3 :
        ubah_umur = int(input("Silahkan input umur baru : "))
        data['umur'] = ubah_umur
        print("Data anda sukses diperbarui")
    elif opsi == 4 :
        ubah_alamat = input("Silahkan input alamat baru : ")
        data['alamat'] = ubah_alamat
        print("Data anda sukses diperbarui")
    elif opsi == 5 :
        print(f"Selamat tinggal {data['nama']}")
        break