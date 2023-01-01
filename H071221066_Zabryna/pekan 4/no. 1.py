#mengembalikan nilai faktorial dari bilangan bulat 

bilangan = int(input("bilangan bulat : "))

def faktorial(bilangan) :
    if bilangan > 1 :
        return bilangan*faktorial(bilangan-1)

    return 1

faktorial = faktorial(bilangan)
print(f'{bilangan}! = {faktorial}')