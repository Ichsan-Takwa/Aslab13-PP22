# gerakan robot

x, y = 0,0

def movement(arah, x, y) :
    if arah == "U" :
        y += 1 
    if arah == "D" :
        y -= 1 
    if arah == "R" :
        x += 1
    if arah == "L" :
        x -= 1 

    return x, y


while True :
    arah = input("U/D/R/L : ")
    if arah == "END" :
        break
    x, y = movement(arah, x, y)
    print(x,y)