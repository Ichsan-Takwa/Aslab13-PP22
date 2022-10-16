def robot(x,y) :
    awal = 1
    while True :
        arah = input()
        if awal == 1 :
            print('0 0')
            awal += 1
        awal+=1
        for i in arah :
            if i == 'R' :
                x += 1
                print(f"{x} {y}")
            elif i == 'L' :
                x -= 1
                print(f"{x} {y}")
            elif i == 'U' :
                y +=1
                print(f"{x} {y}")
            elif i == 'D' :
                y -= 1
                print(f"{x} {y}")
        if arah == "end" :
            break
robot(0,0)