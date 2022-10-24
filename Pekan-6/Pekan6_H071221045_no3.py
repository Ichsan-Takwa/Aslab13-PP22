nama = 20
nim = 12
angkatan = 10

vertikal = [0, nama+1, nama+nim+2, nama+nim+angkatan+3]
header = ["Nama", "NIM", "Angkatan"]

file_nama = input("Masukkan nama file: ")
banyak = int(input("Berapa banyak input: "))

data = [
        {"nama":"henokh", "nim":"H071221045", "angkatan":"2022"},
        {"nama":"jago", "nim":"H071221046", "angkatan":"2022"}
]

with open(file_nama + ".txt") as file:
    count = 0
    mahasiswa = {
        "nama":None,
        "nim":None,
        "angkatan":None
    }
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        
        if count%3 == 0:
            mahasiswa["nama"] = line
        elif count%3 == 1:
            mahasiswa["nim"] = line
        elif count%3 == 2:
            mahasiswa["angkatan"] = line
            data.append(mahasiswa.copy())
        count+=1

data_now = 0
for y in range(3 + (banyak)):
    x = 0
    while x < (nama + angkatan + nim + 4):
        if y == 0 or y == 2:
            if x in vertikal:
                print("+", end="")
            else:
                print("-", end="")
        else:
            if x in vertikal:
                print("|", end="")
            else:
                if y == 1:
                    if x == 2:
                        print(header[0], end="")
                        x += (len(header[0]))
                        print(" ", end="")
                    elif x == nama+3:
                        print(header[1], end="")
                        x += (len(header[1]))
                        print(" ", end="")
                    elif x == nama+nim+4:
                        print(header[2], end="")
                        x += (len(header[2]))
                        print(" ", end="")
                    else:
                        print(" ", end="")
                else:
                    if x == 2: 
                        print(data[data_now]["nama"], end="")
                        x += len(data[data_now]["nama"])

                    if  x == nama+3: 
                        print(data[data_now]["nim"], end="")
                        x += len(data[data_now]["nim"])
                    
                    if  x == nama+nim+4: 
                        print(data[data_now]["angkatan"], end="")
                        x += len(data[data_now]["angkatan"])
                    
                    print(" ", end="")
        x+=1
    if y > 2:
        data_now+=1
    print(end="\n")