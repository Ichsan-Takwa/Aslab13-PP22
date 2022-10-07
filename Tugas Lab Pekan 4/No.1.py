# Nomor 1
# Mahendra Kirana M.B (H071221058)

x = int(input('Masukkan Nilai : '))

def factorial(x) :
    if x == 1 :
        return 1
    elif x < 0 :
        return ('Tak Terdefinisi')
    elif x == 0 :
        return 1
    else :
        return (x * factorial(x-1))

print(factorial(x))
