import requests, bs4, colorama
from colorama import Fore
from bs4      import BeautifulSoup

def adresse_search(name,pren):
    r = requests.get('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={} {}'.format(name,pren), timeout=60)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    target_name = soup.find("a", {"class": "denomination-links pj-lb pj-link"})
    target_addr = soup.find("a", {"class": "adresse pj-lb pj-link"})
    target_phon = soup.find('strong',{'class':'num'})

    try:
        name_full = (target_name.text.strip())
        addr_full = (target_addr.text.replace(', voir sur la carte','').replace('\n',' ').strip())
        phon_full = (target_phon.text.strip())

        if name.lower() in name_full.lower():
            try:
                r = requests.get('https://www.infos-numero.com/ajax/NumberInfo?num={}'.format(phon_full), timeout=60)
                data = r.json()

                type_tel = (data['info']['type'])
                if type_tel == "FIXED_LINE":
                    type_tel = "Fixe"
                carrier = (data['info']['carrier'])
                if len(carrier) <= 1:
                    carrier = 0
                    carrier = None
                localisation = (data['info']['ville'])
                text = {'Phone':phon_full,'Name':name_full,'Adress':addr_full,'Type_tel':type_tel,"Loc_phone":localisation,'carrier':carrier}
                return text
            except:
                return  {'Phone':phon_full,'Name':name_full,'Adress':addr_full,'Type_tel':None,"Loc_phone":None,'carrier':None}
        else:
            return None
    except AttributeError:
        return None
