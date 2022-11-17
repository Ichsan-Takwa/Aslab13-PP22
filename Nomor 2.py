import re

kondisi_ipv4 = r'(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
kondisi_ipv6 = r'(([\dA-Fa-f]{1,4}?\:){7})([\dA-Fa-f]{1,4})$'

n = int(input())
list = []

for i in range (n) :
    s = input()
    list.append(s)

for j in list :
    ipv4 = re.search (kondisi_ipv4, j)
    ipv6 = re.search (kondisi_ipv6, j)
    if ipv4 :
        print('Ipv4')
    elif ipv6 :
        print('Ipv6')
    else :
        print('Bukan IP Address')