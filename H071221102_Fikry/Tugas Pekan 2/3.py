#Program mencari angka berapa yang genap, ganjil, positif, dan negatif
s = input()
a, b, c, d, e = s.split(' ')

p = a.replace('-','')
q = b.replace('-','')
r = c.replace('-','')
s = d.replace('-','')
t = e.replace('-','')

if p.isnumeric() and q.isnumeric() and r.isnumeric() and s.isnumeric() and t.isnumeric():

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    print("masukkan lima angka")

    genap= 0
    ganjil= 0
    positif= 0
    negatif= 0

    if a % 2 == 0:
        genap+= 1
    elif a % 2 == 1:
        ganjil+= 1
    if a > 0:
        positif+= 1
    elif a < 0:
        negatif+= 1

    if b % 2 == 0:
        genap+= 1
    elif b % 2 == 1:
        ganjil+= 1
    if b > 0:
        positif+= 1
    elif b < 0:
        negatif+= 1

    if c % 2 == 0:
        genap+= 1
    elif c % 2 == 1:
        ganjil+= 1
    if c > 0:
        positif+= 1
    elif c < 0:
        negatif+= 1

    if d % 2 == 0:
        genap+= 1
    elif d % 2 == 1:
        ganjil+= 1
    if d > 0:
        positif+= 1
    elif d < 0:
        negatif+= 1

    if e % 2 == 0:
        genap+= 1
    elif e % 2 == 1:
        ganjil+= 1
    if e > 0:
        positif+= 1
    elif e < 0:
        negatif+= 1

    print(f'{genap} Angka Genap')
    print(f'{ganjil} Angka Ganjil')
    print(f'{positif} Angka Positif')
    print(f'{negatif} Angka Negatif')

else:
    print("Inputan tidak valid")
        
