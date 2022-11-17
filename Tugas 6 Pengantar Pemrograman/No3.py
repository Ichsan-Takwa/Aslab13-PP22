
PJ_NAMA = 25 
PJ_NIM = 10
PJ_ANGKATAN = 9
# +--------+-----+---------+
# |Nama    |NIM  | angkatan|
# +--------+-----+---------+
# |  20    | 10  | 4       |
# |  20    | 10  | 4       |


file_name = str(input("nama file : "))
banyak_data = int(input("banyak data: "))

vertikal = [0, PJ_NAMA+1, PJ_NAMA+PJ_NIM+2, PJ_NAMA+PJ_NIM+PJ_ANGKATAN+3]

header = ["Nama","NIM","Angkatan"]

data = [
        {"Nama":"Aris Akhyar Abdillah", "NIM":"H071171505|", "Angkatan":"2017"},
        {"Nama":"Restu Adi Akbar", "NIM":"H071171010|", "Angkatan":"2017"}
]

with open(file_name + ".txt") as f:
    count_line = 0
    mahasiswa = {
        "Nama":None,
        "NIM":None,
        "Angkatan":None
    }
    for line in f:
        print(count_line, line)
        if count_line%3 == 0:
            mahasiswa["Nama"] = line
        if count_line%3 == 1:
            mahasiswa["NIM"] = line
        if count_line%3 == 2:
            mahasiswa["Angkatan"] = line
            data.append(mahasiswa)
        count_line+=1

data_now = 0
for i in range(4+banyak_data):
    j = 0
    while j < PJ_NAMA+PJ_ANGKATAN+PJ_NIM+4:

        if i == 0 or i == 2 or i == banyak_data+4:
            if j in vertikal:
                print("+", end="")
            else :
                print("-", end="")
        else:
            if j in vertikal:
                print("|", end="")
            else :
                if i == 1:
                    
                    if j == 1: 
                        print(header[0], end="")
                        j += len(header[0])

                    if  j == PJ_NAMA+2: 
                        print(header[1], end="")
                        j += len(header[1])
                    
                    if  j == PJ_NAMA+PJ_NIM+3: 
                        print(header[2], end="")
                        j += len(header[2])
                    
                    print(" ", end="")
                else:
                    if j == 1: 
                        print(data[data_now]["Nama"], end="")
                        j += len(data[data_now]["Nama"])

                    if  j == PJ_NAMA+2: 
                        print(data[data_now]["NIM"], end="")
                        j += len(data[data_now]["NIM"])
                    
                    if  j == PJ_NAMA+PJ_NIM+3: 
                        print(data[data_now]["Angkatan"], end="")
                        j += len(data[data_now]["Angkatan"])
                    
                    print(" ", end="")
        j+=1
    if i > 2:
        data_now+=1
        


    print(end="\n")
    