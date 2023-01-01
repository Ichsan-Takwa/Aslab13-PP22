# def toRight(x, y):
#   return x+1, y

# def toLeft(x, y):
#   return x-1, y

# def toUp(x, y):
#   return x, y+1

# def toDown(x, y):
#   return x, y-1

# answer = ""
# x = 0
# y = 0
# while answer != "END":
#   answer = input("Masukkan String Operasi : ")
#   for z in answer:
#     if z == "R":
#       x, y = toRight(x, y)
#       print("x",x,"y",y)
#     elif z == "L":
#       x, y = toLeft(x, y)
#       print("x",x,"y",y)
#     elif z == "D":
#       x, y = toDown(x, y)
#       print("x",x,"y",y)
#     elif z == "U":
#       x, y = toUp(x, y)
#       print("x",x,"y",y)
    
x,y =(0,0)

def movement (arah,x,y) :
  if arah == 'U' :
    y += 1
  if arah == 'D' :
    y -= 1
  if arah == 'L':
    x -= 1
  if arah == 'R':
    x += 1

  return (x,y)

while True :
  arah = input ('U/D/L/R :')
  if arah == 'END' :
    break 
  x,y = movement(arah,x,y)
  print (x,y)
