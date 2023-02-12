from flask import Flask, abort
from data import me, mock_catalog

import json

app = Flask(__name__) # creating a new instance of the class 'Flask'

@app.get("/")
def home():
    return "Hello World!"

@app.get("/about")
def about():
    return "Scott Stevens"

@app.get("/contact/me")
def contact_me():
    return "saseaa37@gmail.com"

################### API --> JSON #########################

@app.get("/api/developer")
def developer():
    return json.dumps(me)

@app.get("/api/developer/address")
def dev_address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    return f'{address["street"]}, #{address["number"]}, {address["city"]}, {address["zipcode"]}'

@app.get("/api/catalog")
def get_catalog(): 
    return json.dumps(mock_catalog)

@app.get("/api/catalog/count")
def count_products():
    count = len(mock_catalog)
    return json.dumps(count)

@app.get("/api/category/<cat>")
def prod_by_category(cat):
    results = []
    for prod in mock_catalog:
        if prod["category"] == cat:
            results.append(prod)

    return json.dumps(results)

@app.get("/api/product/<id>")
def prod_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return abort(404, "Invalid id")

@app.get("/api/product/search/<text>")
def search_product(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)

@app.get("/api/categories")
def get_categories():
    results = []
    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results) 
 
app.run(debug=True)
