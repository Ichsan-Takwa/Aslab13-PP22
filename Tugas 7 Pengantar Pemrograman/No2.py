import re

jumlah_input = int(input())
data = []
for i in range(jumlah_input):
    isi = str(input())
    data.append(isi)

pola0_255 = r'(25[0-5]|2[0-4][0-9]|1[0-9]{1,2}|[1-9]?[0-9])'
syarat_IPV4 = fr'{pola0_255}\.{pola0_255}\.{pola0_255}\.{pola0_255}'

hex_4char = r'[0-9a-fA-F]{1,4}'
syarat_IPV6 = fr'^{hex_4char}:{hex_4char}:{hex_4char}:{hex_4char}:{hex_4char}:{hex_4char}:{hex_4char}:{hex_4char}$'

for i in range(jumlah_input):
    if len(data[i]) <= 32:
        pola1 = re.findall(data[i],pola0_255)
        pola2 = re.findall(data[i],syarat_IPV4)
        if pola1 or pola2:
                print('IPv4')
        else:
            print('Bukan IP Adress')

    elif len(data[i]) <= 128:
        pola3 = re.findall(data[i],syarat_IPV6)
        if pola3:
            print('IPv6')
        else:
            print('Bukan IP Adress')
    else:
        print('Bukan IP Adress')