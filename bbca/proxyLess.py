#specifically monitors for the 5090 FE, dont know how to do a site wide scrape
import requests
import time
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed



def FE_5090(start):

    #api, headers, cookies - needed to access request from bbca
    u = 'https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.simpleproduct.v1%2Bjson&accept-language=en-CA&locations=&postalCode=M6N5G8&skus=18931348%3Bbbyca'
    h = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "priority": "u=1, i",
        "referer": "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-5090-32gb-gddr7-video-card/18931348",
        "sec-ch-ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    c = {
        "_abck": "25CA4FC001478CF794E1185DF7A30665~-1~YAAQpRghF+0vHEmVAQAAHd/UTw3/HCbyvDkSBvsU8bi4rpc4YKhS/Ym+wY/trroSzs7IIzn+Z8HuaBaWJysNJalAm7UoKGQODy08O88Gqmkcwatz4aGhOHDgBEN/EU2lLvDTqm85fYRCY5rryXGiLmjgA4sCa+qaJTM+WbfF+dDBJUb0d0Mt22uLbyhlT785IboGp6+uRHZVZHxQorK210HUL/xWJDyGnfhpNI53E1hWWeXEQ9CZgRnrC3P6kpa4NWVBi5+DvPDl19u2E2buhIBi1xpflDrwMTNVsXjDpaTw4J0LTK09ZTMOVzzkxMBeoGkutawrm11zTfdeFQuqOVcDKnv5EuI81ljUZnj6RCpb6AOQug7jI3GiWNEGOB4NFvh6FD4x2FjDNne9JQ3mPp0sNE0wvk8csS4ztLk8yxqPVSwzHV3BC+mEdA4/1KgFGtM=~-1~-1~-1",
        "bm_sz": "70553F1A0108013DB9E2B8DCC913DA24~YAAQpRghF+4vHEmVAQAAHd/UTxofUzTL+bqvdZLkX1uhLu6KQtGtJAGDUcU0mO87equUx3NMdUrGWto2RhnTnwup7heexk7NySC1KIyiO/h2fdEkcZPL4EnMsAzGEzHFxsx3X0m587a/lurwjkkwqrN5Q/cRbT3EPK74ep5YEai/ke7tUs5e+dopeqdsZt572QMjGJ4ZGcsocjQNRq+FAV0a45zbXt597tl3p/4bk6qgr9Xp99zGQn5pbqYqZrjlj0fBd2Cf0iT6UhI/MUrQUegD84Bwmu/cD9eKNkxq9BEunYjHlkAkkYiV+RBP99DUNBRAt8KO1emiX0HeDknj/5FBkI00Om1b8pnzSsGq+Wb8TXSvnuVcFcmcGTIwJjmk/ryNwE6W~4338999~3622212"
    }


    #x = response object of request, y is json response from x
    x = requests.get(url=u,headers=h,cookies=c)
    y = x.json()['availabilities'][0]['shipping']['purchasable']

    #embed desc w/ link
    emb=DiscordEmbed(title="5090 BBCA FE", description='https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-5090-32gb-gddr7-video-card/18931348', color="e1ffcf")





    if start.upper()=="T":
        while y == False:

            #discord wh object
            ooswh = DiscordWebhook(url=os.getenv('webhook'), content=f'not instock. Purchaseable: {y}')
            print('not in stock.')

            #adding embed
            ooswh.add_embed(emb)
            ooswh.execute()
            time.sleep(30)
            pass

        while y == True:

            inwh = DiscordWebhook(url=os.getenv('webhook'), content=f'instock 5090 fe!!! Purchaseable: {y}')
            print('instock 5090 fe!!!')

            inwh.add_embed(emb)
            inwh.execute()
            time.sleep(30)
            pass

    else:
        pass

load_dotenv()
