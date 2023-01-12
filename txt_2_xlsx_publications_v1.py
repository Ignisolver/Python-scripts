# %%
import os
import re
#%%
name = "KATEDRA CHORÓB WEWNĘTRZNYCH I DIAGNOSTYKI.txt"
os.chdir("data")
for name in os.listdir():
    name = name[:-4]
    file = open(f"{name}.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()

    # %%
    pubs = []
    pub = []
    tags = ['Tytuł oryginału', 'Czasopismo', 'Impact Factor', 'Punktacja MNiSW', 'Autorzy']
    odczyt = True
    for line in lines:
        if re.match("[0-9]+/[0-9]+", line := line.strip()):
            odczyt = True
            if pub:
                pubs.append(pub)
                pub = []

        if line == "Punktacja dyscyplin:":
            odczyt = False

        if odczyt is True and line:
            line = line.split(":", 1)
            pub.append(line)
    pubs.append(pub)

    print(len(pubs))

    #%%
    pub_dicts = []

    for pub in pubs:
        pub_dict = dict.fromkeys(tags, None)
        for line in pub:
            tag = line[0]
            if tag in pub_dict.keys():
                pub_dict[tag] = line[1][:-1] if line[1][-1] == '.' else line[1]
        pub_dicts.append(pub_dict)
    #%%
    print(pub_dicts[1], sep='\n\n\n\n')
    #%%
    for pub in pub_dicts:
        try:
            # pub["Autorzy"].replace(",","#####%%%%%")
            if pub["Autorzy"][-1] == ".":
                pub["Autorzy"] = pub["Autorzy"][:-1]
        except:
            print("no authors")
    #%%
    import csv
    cols = list(tags)
    with open(f"output_csv/{name}_output.csv", 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=cols)
        writer.writeheader()
        for data in pub_dicts:
            writer.writerow(data)

    #%%
    import pandas as pd
    read_file = pd.read_csv(fr'output_csv/{name}_output.csv')
    read_file.to_excel(fr'output_xlsx/{name}.xlsx', index=None, header=True)









