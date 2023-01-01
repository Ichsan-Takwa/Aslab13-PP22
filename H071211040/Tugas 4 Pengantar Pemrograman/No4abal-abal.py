x = 0
y = 0
count = 1
mulai = True
while mulai == True:
   inp = str(input())
   if count == 1 :
      print('0 0')
      count += 1
   for i in inp:
      if i == 'R':
         x += 1
         print(x,y)
      elif i == 'L':
         x -= 1
         print(x,y)
      elif i == 'U':
         y += 1
         print(x,y)
      elif i == 'D':
         y -= 1
         print(x,y)
   if inp == 'end':
      break