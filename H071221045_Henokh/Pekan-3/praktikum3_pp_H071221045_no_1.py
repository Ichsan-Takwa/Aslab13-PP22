x = int(input("Masukkan Nilai X: "))
y = int(input("Masukkan Nilai Y: "))

count = 0

for i in range(1, y + 1):
    print(i, end=' ')
    count+=1
    if count > x - 1:
        print(' ')
        count = 0
