import sys
import random

sys.path.insert(0, "..")
from model.Stock import Stock
from config import url, token;
from json import JSONEncoder
from api.api import get
from datetime import datetime, timedelta


class Collection:

    def __init__(self):
        self.collection = self.randomCurrency();
        self.annualizedReturn = 0;
    
    def randomCurrency(self):
        currencies = [];
        # TODO: Generating 2 currency 
        currencies.append(Stock("usd", random.randint(1,10)));
        currencies.append(Stock("2RG.XFRA", random.randint(1,10)));
        return currencies;
    

    def profit(self, start_date, end_date):
        response = [];
        futureValue = 0;
        initialValue = 0;
        difference_date = (datetime.strptime(end_date, "%Y-%m-%d").date() - datetime.strptime(start_date, "%Y-%m-%d").date()) / timedelta(days=365);
        print(difference_date)
        if int(difference_date) > 1:
            age = int(difference_date);
        else:
            # For annualizedReturn
            age = 1
        try:
            for currency in self.collection:      
                print(url + "?access_key=" + token + "&symbols=" + currency.name + "&date_from=" + start_date + "&date_to=" + end_date)    
                response = get(url + "?access_key=" + token + "&symbols=" + currency.name + "&date_from=" + start_date + "&date_to=" + end_date);
                print(1)
                print(response.json())
                print(2)
                print("currency")
                print(currency)
                print(currency.base_price)
                print(int(currency.base_price))
                print(int(currency.number))
                futureValue = futureValue + (self.calculateRevenue(response.json(), int(currency.base_price)) * int(currency.number));
                initialValue = initialValue + (currency.base_price * currency.number);
            self.annualizedReturn = ( pow( (futureValue/initialValue),(1/age) ) - 1 ) * 100;
            return self;
        except:
            print("Error with API call");
            return
    
    
    def calculateRevenue(self, data, base_price):
        print(base_price)
        revenue = base_price;
        for value in data['data']:
            print(revenue)
            revenue = revenue + (value['close'] - base_price); 
        return revenue;

# subclass JSONEncoder
class CollectionEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__