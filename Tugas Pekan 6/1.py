import os

filecopy = input("Nama file yang di copy: ")
filetarget = input("Nama file yang telah dicopy: ")

cekfile = os.path.isfile(filecopy)

if cekfile == True:
    print("Berhasil")

else:
    print("Gagal")
    exit()
    
nama = filetarget
for i in range(1, 100):
    file1 = os.path.isfile(nama+".txt")

    if file1:
        nama = filetarget + f"({i})"
    else:
        break

with open(filecopy, "r") as file:
    with open(nama+".txt", "x") as hasil:
        for j in file:
            tes = "{:>10}".format(j)
            hasil.writelines(j)
