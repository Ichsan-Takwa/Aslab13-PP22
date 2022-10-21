# # duplikat 2 buah array

array_1 = input("Input array ke-1 : ").split()
array_2 = input("Input array ke-2 : ").split()

duplikat = []
for i in array_1 :
    for j in array_2 :
        if i == j :
             duplikat.append(i)

print(f"Terdapat {len(duplikat)} buah duplikat, yaitu {duplikat}")