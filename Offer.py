from dataclasses import dataclass
from typing import Optional
import json

@dataclass
class Offer:
    model: str
    productionYear: int
    price: int
    localization: str|None

    def serializeToJson(self) -> str:
        return json.dumps([self.model, self.productionYear, self.price, self.localization])
    
    @staticmethod
    def load(json_string) -> Optional['Offer']:
        data = json.loads(json_string)
        try:
            return Offer(*data)
        except:
            return None

def saveOffers(offers: ['Offer'], filename: str):
    with open(filename, 'w+') as fh:
        #serialize to json every offer instance
        offers = list(map(lambda offer: offer.serializeToJson(), offers))
        fh.write(json.dumps(offers))

def loadOffers(filename: str) -> [Optional['Offer']]:
    offers = []
    with open(filename, 'r') as fh:
        #load list of serialized objects
        offersStr = json.loads(fh.read())
        offers = list(map(lambda offer: Offer.load(offer), offersStr))
    return offers