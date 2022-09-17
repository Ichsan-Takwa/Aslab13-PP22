import math

s = int(input("Masukkan Detik : "))
h = math.floor((s/3600)) 
m = math.floor((s%3600)/60)
s1 = (s%3600)%60

print(h,":",m,":",s1)