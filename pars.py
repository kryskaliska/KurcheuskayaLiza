import re
from collections import Counter

fp = open('../access.log','r')
print(fp.readlines(100000))
n = 0
fp.seek(n)
a = len(fp.readlines(5000)) #number of requests
print(a)

fp.seek(n)
res_list = []
logfile = open('../access.log', 'r')
for lines in logfile.readlines(5000):
    ip_patt = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', lines) #pattern ip
    if ip_patt not in res_list:
        res_list.append(ip_patt)
print(res_list)
b = len(res_list)
num_ip = b - 1 #minus initial empty res_list = []
print(num_ip) #number unique ip

fp.seek(n)
browser_list = []
logfile = open('../access.log', 'r')
for lines in logfile.readlines(5000):
    print(lines.split())

    #print(lines.split[-2])
    #spl = lines.split.pop(-2)
    #browser_list = browser_list.append(spl)
#print(browser_list)
    #print(spl[-1])
    #spl_lines = spl[-2]
    #browser_list = browser_list.append(spl_lines)
#print(browser_list)

#z = sorted(browser_list)
#count_Firefox = z.count('Firefox')
#count_Chrome = z.count('Chrome')
#count_Safari = z.count('Safari')
#count_Mozilla = z.count('Mozilla')



fp.close()
print(fp.closed)