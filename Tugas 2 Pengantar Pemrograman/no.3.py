
from unicodedata import numeric


a,b,c,d,e = map(str,input("Masukkan angkanya : ").split())
angkaGanjil = 0
angkaGenap = 0
angkaPositif = 0
angkaNegatif = 0

if a.isnumeric() and b.isnumeric and c.isnumeric and d.isnumeric and e.isnumeric:
    a= int(a)
    b= int(b)
    c= int(c)
    d= int(d)
    e= int(e)
    #a
    if a == 0:
        angkaGenap +=1
    elif a%2 == 0:
        angkaGenap += 1
        if a > 0:
            angkaPositif +=1
        elif a < 0:
            angkaNegatif +=1

    elif a%2 > 0 :
        angkaGanjil +=1
        if a > 0:
            angkaPositif +=1
        elif a < 0:
            angkaNegatif +=1

    # b
    if b == 0:
        angkaGenap +=1
    elif b%2 == 0:
        angkaGenap += 1
        if b > 0:
            angkaPositif +=1
        elif b < 0:
            angkaNegatif +=1

    elif b%2 > 0 :
        angkaGanjil +=1
        if b > 0:
            angkaPositif +=1
        elif b < 0:
            angkaNegatif +=1

    # c
    if c == 0:
        angkaGenap +=1
    elif b%2 == 0:
        angkaGenap += 1
        if c > 0:
            angkaPositif +=1
        elif c < 0:
            angkaNegatif +=1

    elif c%2 > 0 :
        angkaGanjil +=1
        if c > 0:
            angkaPositif +=1
        elif c < 0:
            angkaNegatif +=1

    # d
    if d == 0:
        angkaGenap +=1
    elif d%2 == 0:
        angkaGenap += 1
        if d > 0:
            angkaPositif +=1
        elif d < 0:
            angkaNegatif +=1

    elif d%2 > 0 :
        angkaGanjil +=1
        if d > 0:
            angkaPositif +=1
        elif d < 0:
            angkaNegatif +=1

    if e == 0:
        angkaGenap +=1
    elif e%2 == 0:
        angkaGenap += 1
        if e > 0:
            angkaPositif +=1
        elif e < 0:
            angkaNegatif +=1

    elif e%2 > 0 :
        angkaGanjil +=1
        if e > 0:
            angkaPositif +=1
        elif e < 0:
            angkaNegatif +=1
    print(angkaGenap,"Angka genap")
    print(angkaGanjil, "Angka ganjil")
    print(angkaPositif, "Angka positif")
    print(angkaNegatif, "Angka negatif")

else:
    print("Inputan Tidak Valid")
