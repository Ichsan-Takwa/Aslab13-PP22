print("Selamat datang untuk memulai silahkan input data anda")

a = input("Input Nama : ")
b = input("Input Umur : ")
c = input("Input Alamat : ")

detail = {
    'nama' : a,
    'umur' : b,
    'alamat' : c,
    }

while True:
    print("===========================================================================")
    print(f"Selamat datang {detail['nama']} silahkan pilih opsi")
    print("===========================================================================")
    print('''1. Detail anda)
    2. Ubah Nama
    3. Ubah Umur
    4. Ubah Alamat
    5. Keluar''')
    print("===========================================================================")
    x = int(input("Input Opsi: "))
    print("===========================================================================")
    if x == 1:
        print(f'''Data anda adalah
    Nama: {detail['nama']}
    Umur: {detail['umur']}
    Alamat: {detail['alamat']}''')
    elif x == 2:
        detail['nama'] = input("Silahkan input nama baru: ")
        print("Data anda sukses diperbarui")
    elif x == 3:
        detail['umur'] = input("Silahkan input umur baru: ")
        print("Data anda sukses diperbarui")
    elif x == 4:
        detail['alamat'] = input("Silahkan input alamat baru: ")
        print("Data anda sukses diperbarui")
    elif x == 5:
        print(f"Selamat Tinggal {detail['nama']}")
        quit()
