#%%
from os import chdir
chdir(r"C:\Users\ignsz\Desktop")
with open(r"dane _ewaluacja.txt",'r', encoding="utf8") as plik:
    linie = plik.readlines()
#%%
pubs = [[]]
n = 1
for linia in linie:
    if linia == f'{n}/1489\n':
        n += 1
        pubs.append([])
        continue
    if linia == "\n":
        continue
    else:
        pubs[n-1].append(linia.strip())
del pubs[0]
print(len(pubs))
#%%
from copy import copy
pub_dict = {"INNE":[]}
pub_dicts = []
for pub in pubs:

    curr_pub_dict = copy(pub_dict)
    for line in pub:
        if "Punktacja dyscyplin" in line:
            break
        key_val = line.split(":", 1)
        a = len(key_val)
        if a == 2:
            key, val = key_val
            val = val.replace(",", "##$$##")
            pub_dict.update({key: None})
            curr_pub_dict.update({key: val})
        if len == 1:
            key_val = key_val.replace(",", "##$$##")
            curr_pub_dict["INNE"].append(key_val)
    pub_dicts.append(curr_pub_dict)
#%%
import csv

with open('result.csv', 'w', encoding="utf8", newline='') as f:
    w = csv.DictWriter(f, pub_dict.keys())
    w.writeheader()
    _ = w.writerows(pub_dicts)
#%%
