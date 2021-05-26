from bs4 import BeautifulSoup
import re
import pandas as pd

f = open("/Users/Nishant/Desktop/regex/sample-example.html", 'r')
s = f.read()
soup = BeautifulSoup(s, 'html.parser')

rows = soup.find_all('th')
th = []
ansth = []
for row in rows:
    th.append(re.findall(r">[^><]+<", str(row)))

for t in th:
    for i in t:
        i = i.replace('\n', '')
        i = i.replace(' ', '')
        i = i[1:-1]
        if i:
            ansth.append(i)


rows = soup.find_all('td')
td = []
anstd = []
for row in rows:
    td.append(re.findall(r">[^><]+<", str(row)))

for t in td:
    for i in t:
        i = i.replace('\n', '')
        i = i.replace(' ', '')
        i = i[1:-1]
        if i:
            anstd.append(i)

dict = {}
ind = 0
enum = {}
for i in ansth:
    dict[i] = []
    enum[ind] = i
    ind += 1
ind = 0
for i in anstd:
    dict[enum[ind]].append(i)
    ind += 1
    ind %= len(dict)

table = pd.DataFrame(dict)
table.to_csv('./sample.csv')
