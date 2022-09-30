#konversi nilai dalam bentuk angka ke huruf 

nilai = int(input("nilai : "))

if nilai >= 90:
    print(f"Nilai {nilai} = A")
elif nilai >=80:
    print(f"Nilai {nilai} = B")
elif nilai >=  70:
    print(f"Nilai {nilai} = C")
elif nilai >= 60:
    print(f"Nilai {nilai} = D")
elif nilai >= 40:
    print(f"Nilai {nilai} = E")
elif nilai < 40:
    print(f"Nilai {nilai} = F")
