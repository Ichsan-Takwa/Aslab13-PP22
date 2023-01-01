import re

kondisi_ipv4 = r'(([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$'
kondisi_ipv6 = r'(([\dA-Fa-f]{1,4}?\:){7})([\dA-Fa-f]{1,4})$'

n = int(input())
list = []

for i in range(n):
    s= input()
    list.append(s)

for j in list:
    ipv4 = re.findall(kondisi_ipv4, j)
    ipv6 = re.findall(kondisi_ipv6, j)
    if ipv4:
        print('IPv4')
    elif ipv6:
        print('IPV6')
    else:
        print('Bukan IP Addres')
