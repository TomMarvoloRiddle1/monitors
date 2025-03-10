import json
import requests
from ping import pinger


with open('skuList.json') as list:
    pairs = json.load(list)['cc']

CC_wh = 'https://discord.com/api/webhooks/1348361859698262046/XkPcBEdri44z48WYhkiID9YT2-fGvkK-Or9iSRsFBA1F8hfiHoiam-M9zYUxy4KzaZ7Q'

#3828 Highway 7 East
cookies_markham = {
    'preferloc': 'MU'
}
#1001 Rue Du Marché Central
cookies_quebec = {
    'preferloc': 'MC'
}
#720 Burnhamthorpe Road West
cookies_sauga = {
    'preferloc': 'MI'
}
#19-150 West Drive
cookies_brampton = {
    'preferloc': 'BR'
}


def instore():
    for productName in pairs:
        u = pairs[productName]


        #uses cookie to set store @ markham
        productRequestMarkham = requests.get(url=u,cookies=cookies_markham)
        match productRequestMarkham.text:
            case MarkamHAS if 'Markham Unionville, ON' and 'Available at' in productRequestMarkham.text:
                pinger(wh=CC_wh,tit=f'{productName} - Instock At \n 3828 Highway 7 East',desc=u)
                print('Markham Has Stock')
            case MarkamNO if 'Markham Unionville, ON' and 'Sold Out at' in productRequestMarkham.text:
                print('Markham has no stock')
            case _:
                pass
        
        #Quebec
        productRequestQuebec = requests.get(url=u,cookies=cookies_quebec)
        match productRequestQuebec.text:
            case QuebecHAS if 'Marche Central, QC' and 'Available at' in productRequestQuebec.text:
                pinger(wh=CC_wh,tit=f'{productName} - Instock At \n1001 Rue Du Marché Central',desc=u)
                print('Quebec Has Stock')
            case QuebecNO if 'Marche Central, QC' and 'Sold Out at' in productRequestQuebec.text:
                print('Quebec has no stock')
            case _:
                pass


        #Sauga
        productRequestSauga = requests.get(url=u,cookies=cookies_sauga)
        match productRequestSauga.text:
            case SaugaHAS if 'Mississauga, ON' and 'Available at' in productRequestSauga.text:
                pinger(wh=CC_wh,tit=f'{productName} - Instock At \n720 Burnhamthorpe Road West',desc=u)
                print('Sauga Has Stock')
            case SaugaNO if 'Mississauga, ON' and 'Sold Out at' in productRequestSauga.text:
                print('Sauga has no stock')
            case _:
                pass


        #Brampton
        productRequestBrampton = requests.get(url=u,cookies=cookies_brampton)
        match productRequestBrampton.text:
            case BramptonHAS if 'MissisBrampton, ON' and 'Available at' in productRequestBrampton.text:
                pinger(wh=CC_wh,tit=f'{productName} - Instock At \n19-150 West Drive',desc=u)
                print('Brampton Has Stock')
            case BramptonNO if 'MissisBrampton, ON' and 'Sold Out at' in productRequestBrampton.text:
                print('Brampton has no stock')
            case _:
                pass
        

# instore()