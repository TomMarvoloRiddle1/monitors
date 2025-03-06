import requests
import time

#replace w/ whatever API url from product page to be monitored
u = 'https://www.canadacomputers.com/en/powered-by-nvidia/268187/gigabyte-aorus-geforce-rtx-5090-master-ice-32g-gv-n5090aorusm-ice-32gd.html'

#monitor for HTML not JSON

while True:
    if 'Available to Ship' in (requests.get(u)).text:
        print('instock')
        time.sleep(30)
    elif 'Sold out online' in (requests.get(u)).text:
        print('oos')
        time.sleep(30)
    else:
        print('broken')