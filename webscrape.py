import requests
from bs4 import BeautifulSoup
from Offer import Offer

def scrapeOffers() -> ['Offer']:
    url = 'https://www.otomoto.pl/osobowe/bialystok?search%5Bdist%5D=50'
    result = requests.get(url)

    html = result.content
    soup = BeautifulSoup(html, "html.parser")

    def getLocalisation(listing) -> str|None:
        detailsList = listing.find('dl', class_=['ooa-1o0axny', 'e1ajxysh14'])
        if detailsList == None or len(detailsList) == 0:
            return None
        localisationData = detailsList.contents[0].find('p')
        if localisationData != None:
            return localisationData.text

    listings = soup.select('article.ooa-yca59n.e1ajxysh0')
    offers = []
    for listing in listings:
        model = listing.find('h1', class_=['e1ajxysh9', 'ooa-1ed90th','er34gjf0']).contents[0].text
        productionYear = listing.find('dd', class_=['1omlbtp', 'e1ajxysh13'], attrs={'data-parameter': 'year'}).text
        price = listing.find('h3', class_='e1ajxysh16 ooa-1n2paoq er34gjf0'.split(' ')).text.replace(' ', '')
        localization = getLocalisation(listing)
        try:
            offers.append(Offer(model, int(productionYear), int(price), localization))
        except:
            None
    return offers