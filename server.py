from flask import Flask
from data import me

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



################### APT -> JSON #########################



@app.get("/api/developer")
def developer():
    return json.dumps(me)


@app.get("/api/developer/address")
def dev_address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    return f'{address["street"]}, #{address["number"]}, {address["city"]}, {address["zipcode"]}'


app.run(debug=True)