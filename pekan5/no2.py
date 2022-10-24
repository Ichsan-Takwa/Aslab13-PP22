# from argparse import ArgumentDefaultsHelpFormatter


# print('Selamat datang! Untuk memulai silahkan input data anda.')
# nama : input ('Input Nama :')
# umur : int(input('Input Umur :'))
# alamat = input ( 'Input Alamat :')

# dict_profile = {
#     'nama' : nama,
#     'umur' : umur,
#     'alamat ' : alamat

# }

# while True :
#     print('='*60)
#     print(f"Selamat Datang{dict_profile['nama']}, silahkan pilih opsi")
#     print('='*60)
#     print('1. Detail anda')
#     print('2. Ubah nama')
#     print('3. Ubah umur')
#     print('4. Ubah alamat')
#     print('5. keluar')
#     print('='*60)
#     try:
#         opsi= int(input('input opsi'))
#     except :
#         print ('opsi salah')
#     print('='*60)
#     if opsi<=0 or opsi>5 :
#         print('opsi salah')
#     elif opsi==1:
#         print('Data anda salah')
#         print(f"nama:{dict_profile.get('nama')}")
#         print(f"Umur: {dict_profile.get('umur')}")
#         print (f"Alamat:{dict_profile.get('alamat')}")
#     elif opsi==2 :
#         rename= input("silahkan input nama baru:")
#         dict_profile['nama']=rename
#         print("data anda sukses diperbaharui")
#     elif opsi==3:
#         reage= input('silahkan input umur baru:')
#         dict_profile['umur']=reage
#         print("data anda sukses diperbaharui")
#     elif opsi==4:
#         readress=input("silahkan input alamat baru:")
#         dict_profile['alamat']= readress
#         print('data anda diperbaharui')
#     elif opsi==5 :
#         print(f"selamat tinggal{dict_profile['nama']}")
#         break

print("Selamat datang! untuk memulai silahkan input data Anda")
Nama = input("Input nama : ")
Umur = int(input("Input umur : "))
Alamat = input("Input alamat : ")

dict_data = {
    "nama" : Nama, 
    "umur" : Umur, 
    "alamat" : Alamat
    }

while True :
    print("="*50)
    print(f"Halo {dict_data['nama']} silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
    print("="*50)

    
    opsi = int(input("Input opsi : "))

    print("="*50)

    if opsi == 1 :
        print("Data anda adalah : ")
        print(f"Nama : {dict_data['nama']}")
        print(f"Umur : {dict_data['umur']}")
        print(f"Alamat : {dict_data['alamat']}")
    elif opsi == 2 :
        ubah_nama = input("Silahkan input nama baru : ")
        dict_data['nama'] = ubah_nama
        print("Data anda sukses diperbarui")
    elif opsi == 3 :
        ubah_umur = int(input("Silahkan input umur baru : "))
        dict_data['umur'] = ubah_umur
        print("Data anda sukses diperbarui")
    elif opsi == 4 :
        ubah_alamat = input("Silahkan input alamat baru : ")
        dict_data['alamat'] = ubah_alamat
        print("Data anda sukses diperbarui")
    elif opsi == 5 :
        print(f"Selamat tinggal {dict_data['nama']}")
        break