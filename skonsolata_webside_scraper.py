from requests import get
from bs4 import BeautifulSoup as bs
kom = "Komentarz:"
end  = "Twój adres e-mail nie zostanie opublikowany"
url = "https://www.skkonsolata.pl/?page_id={}&page={}"
mt = {"page_id": 14450,"start_nr":2, "end_nr":163}
mk = {"page_id": 14469,"start_nr":2, "end_nr":109}
lk = {"page_id": 14481,"start_nr":2, "end_nr":193}
j = {"page_id": 14518,"start_nr":2, "end_nr":74}
ew = (mt,mk,lk,j)
with open("komentarze.txt","w",encoding="utf-8") as file:
    for ewan in ew:
        for nr in range(ewan["start_nr"], ewan["end_nr"]+1):
            response = get(url.format(ewan["page_id"],nr))
            html = bs(response.text)
            double_next = True
            if ewan["page_id"] == 14518:
                for p in html.find_all("p"):
                    sp = str(p)
                    if end in sp:
                        break
                    if kom in sp:
                        file.write(str(p.next.next) + '\n')
                    else:
                        file.write(str(p.next) + '\n')
            else:
                for p in html.find_all("p"):
                    sp = str(p)
                    if end in sp:
                        break
                    if double_next:
                        file.write(str(p.next.next) + '\n')
                    else:
                        file.write(str(p.next) + '\n')
                    if kom in sp:
                        double_next = False
            file.write("----------------------------------------------------------------------------")
        file.write("""
        #######################################################################
        ##################
        ##################
        ##################
        ##################
        #######################################################################
        """)


