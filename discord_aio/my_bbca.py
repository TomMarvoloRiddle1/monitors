import requests
import json
from ping import pinger


#loads skuList.json for prodName:SKU
with open('skuList.json') as list:
    skuList = json.load(list)

bbca_webhook = 'https://discord.com/api/webhooks/1345259311147778080/yfudLTWRc89bS8jtDtcvv12wJRH_kz7jmSjrUpzByA-u0AFT4zPqdhFGnSG8Khl9h6XP'


h = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}


#add try catch/except
#it is currently iterating to check each sku in order of json, learn concurrency and integrate async + await to check skus
def checkResponse():
    for productName in skuList['bbca']:
        sku = skuList['bbca'][productName]
        u = f'https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.simpleproduct.v1%2Bjson&accept-language=en-CA&locations=&postalCode=M5J&skus={sku}'
        StockRequest = requests.get(url=u,headers=h)
        StockResponse = StockRequest.json()['availabilities'][0]['shipping']['purchasable']

        if StockResponse == True:
            pinger(wh=bbca_webhook,tit=f"{productName}", desc=f'''stock status: {StockResponse} 
{u}''')
            print(productName, StockResponse)
        elif StockResponse == False:
            print(productName, StockResponse)