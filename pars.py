import re

from collections import Counter
fp = open('access.log','r')
n = 0
fp.seek(n)
a = len(fp.readlines())
print(a)
fp.seek(n)
res_list = []
logfile = open('access.log', 'r')
for lines in logfile.readlines(5000):
    ip_patt = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', lines)
    if ip_patt not in res_list:
        res_list.append(ip_patt)
print(res_list)
b = len(res_list)
num_ip = b - 1
print(num_ip)

d = {'Mozilla':'1',
    'Opera':'2',
    'Google Chrome':'3',
    'Safari':'4',
    'Internet Explorer':'5',
    'Яндекс':'6',
    'Edge':'7'
}
i = 0
for lines in logfile.readlines():
    for key in d:
        if key in lines[-30:]:
            i = i + 1
print(i)
fp.close()
print(fp.closed)