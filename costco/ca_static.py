#unique request url

import requests

u = 'https://ecom-api.costco.com/ebusiness/inventory/v1/inventorylevels/availability/v2/5350113?destinationState=AB&destinationPostalCode=T1X%201H4&destinationCountryCode=CA&quantity=1&orderItemId=0&shippingCodes=UPG&action=EDD'
h = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.8",
    "client-identifier": "481b1aec-aa3b-454b-b81b-48187e28f205",
    "connection": "keep-alive",
    "costco.env": "ECOM",
    "costco.service": "restInventory",
    "host": "ecom-api.costco.com",
    "origin": "https://www.costco.ca",
    "referer": "https://www.costco.ca/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}



mon = requests.get(url=u, headers=h)

mon.json()['availableForSale']

#if above = True, instock