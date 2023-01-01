array1 = [1,2,3,4,5]
array2 = [6,2,3,7,8]

hasil = []
for i in array1:
    for j in array2:
        if i == j:
            a = i
            hasil.append(a)
jumlah = len(hasil)
x = str(hasil)
x = x[1:-1]
print(f'Terdapat {jumlah} buah duplikat yaitu ({x})')