from webscrape import scrapeOffers
from Offer import loadOffers, saveOffers

#code sample
offers = scrapeOffers()
print(f'Scraped {len(offers)}!')

path = 'offers.json'
saveOffers(offers, path)
print('Saved offers')

offers = loadOffers(path)
print(f'Loaded {len(offers)}!')