Harga = int(input('Masukkan harga:'))
Bayar = int(input('Maaukkan nominal:'))
kembalian = Harga - Bayar

uang = [100000,50000,20000,10000,5000,2000,1000,500]

for i in uang :
    pembagian_kembalian = kembalian//i
    print (f'{int(pembagian_kembalian)}uang Rp.{i}')
    kembalian = kembalian-(pembagian_kembalian*i)