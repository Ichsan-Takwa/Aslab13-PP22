nilai = int(input("Nilai = "))

if nilai >= 90 and nilai >= 100:
    print(f"Nilai {nilai} = A")
elif nilai >= 80:
    print(f"Nilai {nilai} = B")
elif nilai >= 70:
    print(f"Nilai {nilai} = C")
elif nilai >= 60:
    print(f"Nilai {nilai} = D")
elif nilai >= 40:
    print(f"Nilai {nilai} = E")
elif nilai < 40:
    print(f"Nilai {nilai} = F")
else:
    print("data tidak valid")
