def faktorial(n): 
    if n==1 or n==0:
        return 1
    elif n < 0:
        return "error" 
    else:
        return (n * faktorial(n - 1)) 
  
angka = int(input("Masukkan angka: ")) 
print(f"Faktorialnya adalah: {faktorial(angka)}")