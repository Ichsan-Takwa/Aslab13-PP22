def matriks(satu):
    mat = []
    for x in range(2):
        mat.append([])
        for y in range(2):
            tes = int(input(f"Input nilai matriks {satu} index {x+1},{y+1}: "))
            mat[x].append(tes)
    return mat

def kalimatriks(mat1, mat2):
    hasil = []
    for y in range (2):
        total = []
        for x in range (2):
            kali = mat1[y][0] * mat2[0][x] + mat1[y][1] * mat2[1][x]
            total.append(kali)
        hasil.append(total)
    return hasil

matriks1 = matriks("pertama")
matriks2 = matriks("kedua")
hasilkali = kalimatriks(matriks1, matriks2)

print(f'{matriks1[0]} x {matriks2[0]} = {hasilkali[0]}')
print(f'{matriks1[1]}   {matriks2[1]}   {hasilkali[1]}')
