#Program menghitung tagihan listrik

golongan= input("golongan = ")
daya= float(input("Daya = "))
pemakaian= float(input("Pemakaian = "))

match golongan:
    case "R1":
        if daya == 900:
            jumlah_tagihan = pemakaian * 1352
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        elif daya == 1300 or daya == 2200:
            jumlah_tagihan = pemakaian * 1444.70
            print (f"> jumlah tagihan anda: Rp {jumlah_tagihan:,}")
        else:
            print("data tidak valid")
    
    case "R2":
        if daya >=3500 and daya <=5500:
            jumlah_tagihan = pemakaian * 1699.53
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        else:
            print("data tidak valid")

    case "R3":
        if daya >=6600:
            jumlah_tagihan = pemakaian * 1699.53
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        else:
            print("data tidak valid")
    
    case "B2":
        if daya >=6600 and daya <=200000:
            jumlah_tagihan = pemakaian * 1444.70
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        else:
            print("data tidak valid")

    case "B3":
        if daya >=200000:
            jumlah_tagihan = pemakaian * 1114.74
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        else:
            print("data tidak valid")

    case "I3":
        if daya >=200000:
            jumlah_tagihan = pemakaian * 1314.12
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        else:
            print("data tidak valid")

    case "P1":
        if daya >=6600 and daya <=200000:
            jumlah_tagihan = pemakaian * 1523.28
            print ("jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace("," , ".").replace("/" , ","))
        else:
            print("data tidak valid")

    case _:
        print("data tidak valid")
      
