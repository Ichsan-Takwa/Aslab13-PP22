import re

jumlah_input = int(input())
data = []
for i in range(jumlah_input):
    isi = str(input())
    data.append(isi)

syarat_IPV4 = r'(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])'
syarat_IPV6 = r"[a-zA-Z[02468]"

for i in range(jumlah_input):
    if len(data[i]) <= 32:
            pola1 = re.findall(data[i],syarat_IPV4)
            print(pola1)
            print('IPv4')
    else:
        print('Bukan IP Address')
