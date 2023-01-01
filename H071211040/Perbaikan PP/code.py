prima_awal = 2
angka_akhir = int(input('Panjang Angka: '))
 
list_angka = [i for i in range(prima_awal, angka_akhir +1 )]
 
bilangan_prima = []
for j in list_angka:
    if (j==2 or j==3 or j==5 or j==7) or (j%2 != 0 and j%3 != 0 and j%5 != 0 and j%7 != 0):
        bilangan_prima.append(j)

cetak_bilangan_prima = ', '.join(map(str,bilangan_prima))

print(f'Terdapat {len(bilangan_prima)} prima dari {prima_awal} sampai {angka_akhir}, yaitu: {cetak_bilangan_prima} ')