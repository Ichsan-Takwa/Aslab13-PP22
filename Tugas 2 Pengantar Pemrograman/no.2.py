from dataclasses import replace

golongan = str(input("Golongan = "))
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

a = 1352*pemakaian
a = "{:,.2f}".format(a)
a1,a2 = a.split(".")
a1 = a1.replace(",",".")
a = a1+','+a2

b = 1444.70*pemakaian
b = "{:,.2f}".format(b)
b1,b2 = b.split(".")
b1 = b1.replace(",",".")
b = b1+','+b2

c = 1699.53*pemakaian
c = "{:,.2f}".format(c)
c1,c2 = c.split(".")
c1 = c1.replace(",",".")
c = c1+','+c2

d = 1114.74*pemakaian
d = "{:,.2f}".format(d)
d1,d2 = d.split(".")
d1 = d1.replace(",",".")
d = d1+','+d2

e = 1314.12*pemakaian
e = "{:,.2f}".format(e)
e1,e2 = e.split(".")
e1 = e1.replace(",",".")
e = e1+','+e2

f = 1523.28*pemakaian
f = "{:,.2f}".format(f)
f1,f2 = f.split(".")
f1 = f1.replace(",",".")
f = f1+','+f2


if golongan == "R1":
    if daya == 900 or daya == 1300:
        print("Jumlah tagihan anda :",a)
    elif daya == 2200:
        print("Jumlah tagihan anda : ",b)
    else:
        print("Data tidak valid")
        

elif golongan == "R2":
    if daya >= 3500 and daya <= 5500:
        print("Jumlah tagihan anda : ",c)
    else:
        print("Data tidak valid")

elif golongan == "R3":
    if daya >= 6600:
         print("Jumlah tagihan anda : ",c)
    else:
        print("Data tidak valid")

elif golongan == "B2":
    if daya >= 6600 and daya <= 200000:
        print("Jumlah tagihan anda : ",b)
    else:
        print("Data tidak valid")

elif golongan == "B3":
    if daya > 200000:
        print("Jumlah tagihan anda : ",d)
    else:
        print("Data tidak valid")

elif golongan == "I3":
    if daya >= 200000:
        print("Jumlah tagihan anda : ",e)
    else:
        print("Data tidak valid")

elif golongan == "P1":
    if daya >= 6600 and daya <= 200000:
        print("Jumlah tagihan anda : ",f)
    else:
        print("Data tidak valid")

else:
    print("Data tidak valid")
