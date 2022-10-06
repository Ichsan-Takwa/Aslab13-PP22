def robot(gerak):
    x, y = 0, 0
    while True:
        if gerak == "END":
            print("\nRobot Dihentikan")
            break
        else:
            l = len(gerak)
            for i in range(l):
                if gerak == "U":
                    y = y + 1
                elif gerak == "D":
                    y = y - 1
                elif gerak == "L":
                    x = x - 1
                elif gerak == "R":
                    x = x + 1            
                print(f"\nPosisi: x{(x)}, y{(y)}")
        gerak = input("\nPilih Gerakan (U/D/L/R): ")

            
    
mulai = input("Pilih Gerakan (U/D/L/R): ")
robot(mulai)