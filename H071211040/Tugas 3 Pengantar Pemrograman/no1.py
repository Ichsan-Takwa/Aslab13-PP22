x = int(input("Masukka Angka Mendatar : "))
y = int(input("Masukkan Angka Terakhir : "))

if x<y:
    for i in range(y):
        if (i+1)%x != 0:
            print(i+1,end=" ")
        else:
            print(i+1)
else:
    print("Inputan Tidak Valid")