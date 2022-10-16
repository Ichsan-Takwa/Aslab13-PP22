def movement(move, x, y):
    if move == "R":
        x += 1
    if move == "L":
        x -= 1
    if move == "U":
        y += 1
    if move == "D":
        y -= 1
    return x, y

x, y = 0, 0

while True:
    perintah = input("R, L, U, D: ")
    if perintah == 'END' :
        break
    x, y =movement(perintah, x, y)
    print(x, y)


