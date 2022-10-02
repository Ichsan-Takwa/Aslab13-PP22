# NOMOR 1 PRAKTIKUM PEKAN 3
# MAHENDRA KIRANA M.B(H071221058)

x = int(input("x : "))
y = int(input("y ; "))

for i in range(1, y+1) :
    print(i, end = " ")
    if i % x == 0 :
        print()
