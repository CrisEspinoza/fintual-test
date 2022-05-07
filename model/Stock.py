import sys

sys.path.insert(0, "..")
from api.api import get
from datetime import datetime , timedelta
from config import url, token;

class Stock:

    def __init__(self, name, number):
        self.name = name;
        self.number = number;
        # TODO; 15 days ago I bought
        self.base_price = self.price((datetime.now() - timedelta(15)).strftime("%Y-%m-%d"));
    
    def price(self, date):
        try:
            response = get(url + "/" + date + "?access_key=" + token + "&symbols=" + self.name);
            return response.json()['data'][0]['close'];
        except:
            print("Error with API call");
            return 
    
