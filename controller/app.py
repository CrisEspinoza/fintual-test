import sys

sys.path.insert(0, "..")
from flask import Flask, request, jsonify
from model.Collection import Collection, CollectionEncoder
from config import port, host, app, url, token;
from api.api import get

app = Flask(app)

@app.route('/revenue' ,methods=['GET'])
def revenue():
    start_date = request.args.get('start_date');
    end_date = request.args.get('end_date');
    collection = Collection();
    collection = collection.profit(start_date,end_date);
    return CollectionEncoder().encode(collection);

@app.route('/price' ,methods=['GET'])
def price():
    currency = request.args.get('currency');
    date = request.args.get('date');
    response = get(url + "/" + date + "?access_key=" + token + "&symbols=" + currency);
    return response.json();


# Ejecutar servidor
if __name__ == '__price__' or '__revenue__' or '__annualized__':
    app.run(host=host, port=port);