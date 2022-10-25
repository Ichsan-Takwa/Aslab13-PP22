a = set(map(int,input('Inpur Array Ke 1 :').split()))
b = set(map(int,input('Inpur Array Ke 2 :').split()))

duplikat = tuple(a & b)

print(f'Terdapat {len(duplikat)} buah duplikat yaitu {duplikat}')