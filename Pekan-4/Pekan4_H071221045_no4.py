def robot(gerak, x, y):
    
    l = len(gerak)
    for i in range(l):
        if gerak[i] == "U":
            y+=1
        elif gerak[i] == "D":
            y-=1
        elif gerak[i] == "L":
            x-=1
        elif gerak[i] == "R":
            x+=1
    print(f"\nPosisi: x{(x)}, y{(y)}")
    return x, y
    
x, y = 0, 0

while True:
    mulai = input("Pilih Gerakan (U/D/L/R): ")
    if mulai == "END":
        print("\nRobot Dihentikan")
        break
    else:
        x, y = robot(mulai, x, y)
