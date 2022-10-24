matriks1 = []
matriks2 = []
for i in range(2):
    matriks1.append([])
    for j in range(2):
        a = int(input(f'Input nilai matriks pertama index {i+1},{j+1}: ' ))
        matriks1[i].append(a)
# print(matriks1)
for i in range(2):
    matriks2.append([])
    for j in range(2):
        b = int(input(f'Input nilai matriks kedua index {i+1},{j+1}: ' ))
        matriks2[i].append(b)

hasil1 = [matriks1[0][0]*matriks2[0][0] + matriks1[1][1]*matriks2[1][1], matriks1[0][0]*matriks2[0][0] + matriks1[1][1]*matriks2[1][1]]  
hasil2 = [matriks1[1][0]*matriks2[1][0] + matriks1[0][1]*matriks2[1][0], matriks1[1][0]*matriks2[1][0] + matriks1[0][1]*matriks2[1][0]]
# print(hasil)
print('Hasil perkalian matriks')
print(f'| {matriks1[0][0]}, {matriks1[0][1]} | x | {matriks2[0][0]}, {matriks2[1][0]} | = | {hasil1}  | ')
print(f'| {matriks1[1][0]}, {matriks1[1][1]} | x | {matriks2[1][0]}, {matriks2[1][1]} | = | {hasil2}  | ')
