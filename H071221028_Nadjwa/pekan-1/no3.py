input('Nama: ')
a = float(input('Gaji pokok: '))
b = float(input('Total penjualan: '))
#menggunakan float fungsi ini akan mengubah argumennya yang berupa bilangan menjadi tipe float atau bilangan desimal
c = b * 0.15
d = round(a + c,2)
#round untuk membulatkan angka

print('TOTAL = $',d)

