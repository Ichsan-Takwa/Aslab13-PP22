# Mahendra Kirana M.B
# H071221058

file1 = input()
file2 = input()

try :
    f = open(f"{file1}.txt","r")
    c = f.read()

    w = open(f"{file2}.txt","w")
    w.write(c)
except :
    print('Gagal')
