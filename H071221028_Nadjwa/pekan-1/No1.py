#menghitung panjang kapal
import math  
#memasukkan impor math karena akan menggunakan rumus matematika unutk mencari panjang dr sudut kapal

h= int(input('masukkan h:')) 
a= int(input('masukkan a:'))
b= int(input('masukkan b:'))
#menggunakan int karena akan menginput angka menghitung panjang kapal

m= round(math.tan(b+a)*h,1)
n= round(math.tan(a-b)*h,1)
x= m-n
#memaukkan rumus math.tan untuk mengembalikan nilai phi
#string 1 setelah, untuk membulatkan hasil agar tidak terlalu panjang hasilnya
print('maka panjang kapal:', str(x)+'m')
#memasukkan perintah print, hasil dari x, dan menambahkan string m agar outputnya menampilkan huruf m dibelakang

