a = list(input("Input array ke 1: ").split(" "))
b = list(input("Input array ke 2: ").split())

duplikat = []

for i in a:
    for j in b:
        if i == j:
            duplikat.append(i)
print(f"terdapat {len(duplikat)} duplikat yaitu {duplikat}")

