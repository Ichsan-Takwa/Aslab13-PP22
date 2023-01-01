print('Selamat datang untuk memulai silahkan input data anda')
data = {}
data['nama'] = input('Input Nama : ')
data['umur'] = input('Input umur : ')
data['alamat'] = input('Input alamat : ')

print('='*60)
while True:
    print('Selamat datang' ,data['nama'], 'silahkan pilih opsi')
    print('='*60)
    print('1. Detatil anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar')
    print('='*60)

    inp = int(input("Input opsi: "))
    if inp == 1:
        print('Data anda adalah')
        print('Nama : ',data['nama'])
        print('Umur : ',data['umur'])
        print('Alamat : ',data['alamat'])
    elif inp == 2:
       data['nama'] = str(input('Silahkan Input nama baru : '))
       print('Data anda sukses diperbarui')
    elif inp == 3:
        data['umur'] = str(input('Silahkan Input umur baru : '))
        print('Data anda sukses diperbarui')
    elif inp == 4:
        data['alamat'] = str(input('Silahkan Input alamat baru : '))
        print('Data anda sukses diperbarui')
    elif inp == 5:
        print('Selamat Tinggal', data['nama'])
        break
    else:
        print('Inputan Tidak Valid')
