#menghitung hasil perkalian matriks

mat1 = []
mat2 = []

def matriks1():
    for a in range(2):
        mat_a = []
        for b in range(2):
            m_1 = int(input(f'Input nilai matriks pertama index {a+1},{b+1} : '))
            mat_a.append(m_1)
        mat1.append(mat_a)
    return mat1
    
def matriks2():
    for a in range(2):
        mat_a = []
        for b in range(2):
            m_2 = int(input(f'Input nilai matriks kedua index {a+1},{b+1} : '))
            mat_a.append(m_2)
        mat2.append(mat_a)
    return mat2

matriks = [[0,0], 
           [0,0]]

def hasilkali():
    matriks[0][0] = (mat1[0][0] * mat2[0][0]) + (mat1[0][1] * mat2[1][0])
    matriks[0][1] = (mat1[0][0] * mat2[0][1]) + (mat1[0][1] * mat2[1][1])
    matriks[1][0] = (mat1[1][0] * mat2[0][0]) + (mat1[1][1] * mat2[1][0])
    matriks[1][1] = (mat1[1][0] * mat2[0][1]) + (mat1[1][1] * mat2[1][1])

    print("Hasil perkalian matriks : ")
    print(f'[{(mat1[0][0])} {(mat1[0][1])}] x [{(mat2[0][0])} {(mat2[0][1])}] = [{(matriks[0][0])} {(matriks[0][1])}]')
    print(f'[{(mat1[1][0])} {(mat1[1][1])}]   [{(mat2[1][0])} {(mat2[1][1])}]   [{(matriks[1][0])} {(matriks[1][1])}]')

    return matriks

matriks1()
matriks2()
hasilkali()