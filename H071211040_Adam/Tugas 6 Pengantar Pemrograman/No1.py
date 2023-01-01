File_Name = str(input())
File_Name_Copy = str(input())

file = open(File_Name + '.txt','r')
data = file.read()
file.close()

with open(File_Name_Copy + '.txt','w') as file:
    file.write(data)
print('Berhasil')