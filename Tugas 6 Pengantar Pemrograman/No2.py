file = open('Latihan1.txt','w')
file.write('Baris pertama\n')
file.write('Baris kedua \n')
file.write('Dan Seterusnya... \n')

file.close()

File_Name = input()
File_Name_Copy = input()

file = open(File_Name + '.txt','r')
data = file.read()
file.close()

Line1 = 'Baris pertama'
Line2 = 'Baris kedua \n'
Line3 = 'Dan Seterusnya... '
data1 = '\n{:>15}'.format(Line1)
data2 = '\n{:>20}'.format(Line2)
with open(File_Name_Copy + '.txt','a') as file:
    file.write(data1)
    file.write(data2)
    file.write(Line3)
print('\nBerhasil')